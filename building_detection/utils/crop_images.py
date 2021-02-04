"""
Utilities for creating test data
based on: 0.12/rastervision_pytorch_backend/rastervision/pytorch_backend/examples/utils.py
"""


import os
import tempfile

import rasterio
from rastervision.aws_s3 import S3FileSystem  # pylint: disable=import-error
from rastervision.core import Box  # pylint: disable=import-error
from rastervision.core.data import GeoJSONVectorSourceConfig, RasterioCRSTransformer  # pylint: disable=import-error
from rastervision.pipeline.file_system import (  # pylint: disable=import-error
    file_exists,
    get_local_path,
    json_to_file,
    make_dir,
    upload_or_copy,
)
from shapely.geometry import mapping, shape
from shapely.ops import transform
from shapely.strtree import STRtree


def save_crop(image_uri, window, crop_uri):
    """
    Save the image crop

    @param image_uri: URI of original image
    @type  image_uri: str
    @param window: bbox
    @type  window: astervision.core.box.Box
    @param crop_uri: URI of cropped image to save
    @type  crop_uri: str
    """

    img_dataset = rasterio.open(image_uri)
    rasterio_window = window.rasterio_format()
    im = img_dataset.read(window=rasterio_window)

    with tempfile.TemporaryDirectory() as tmp_dir:
        crop_path = get_local_path(crop_uri, tmp_dir)
        make_dir(crop_path, use_dirname=True)

        meta = img_dataset.meta
        meta["width"], meta["height"] = window.get_width(), window.get_height()
        meta["transform"] = rasterio.windows.transform(rasterio_window, img_dataset.transform)

        with rasterio.open(crop_path, "w", **meta) as dst:
            dst.colorinterp = img_dataset.colorinterp
            dst.write(im)

        upload_or_copy(crop_path, crop_uri)


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def crop_image(
    image_uri,
    image_crop_uri,
    label_uri=None,
    label_crop_uri=None,
    size=600,
    min_features=10,
    vector_labels=True,
    class_config=None,
):
    """
    Crop an image to use for testing.
    If label_uri is set, the crop needs to cover >= min_features.

    @param image_uri: URI of original image
    @type  image_uri: str
    @param image_crop_uri: URI of cropped image to save
    @type  image_crop_uri: str
    @param label_uri: optional URI of GeoJSON label file
    @type  label_uri: str
    @param size: height and width of crop
    @type  size: int
    @param min_features: Min number features to be included in crop
    @type  min_features: int
    @param vector_labels: Is vector label (as opposed to raster)
    @type  vector_labels: bool
    @param class_config: class that is being predicted. Not required
    @type  class_config: None
    """

    if not file_exists(image_crop_uri):
        print("Saving test crop to {}...".format(image_crop_uri))
        old_environ = os.environ.copy()
        try:
            request_payer = S3FileSystem.get_request_payer()
            if request_payer == "requester":
                os.environ["AWS_REQUEST_PAYER"] = request_payer
            img_dataset = rasterio.open(image_uri)
            height, width = img_dataset.height, img_dataset.width

            extent = Box(0, 0, height, width)
            windows = extent.get_windows(size, size)
            if label_uri and vector_labels:
                crs_transformer = RasterioCRSTransformer.from_dataset(img_dataset)
                geojson_config = GeoJSONVectorSourceConfig(uri=label_uri, default_class_id=0, ignore_crs_field=True)
                vector_source = geojson_config.build(class_config, crs_transformer)
                geojson = vector_source.get_geojson()
                geometries = []
                for f in geojson["features"]:
                    geometry = shape(f["geometry"])
                    geometries.append(geometry)
                tree = STRtree(geometries)

            def p2m(x, y):
                return crs_transformer.pixel_to_map((x, y))

            for window in windows:
                use_window = True
                if label_uri and vector_labels:
                    window_polys = tree.query(window.to_shapely())
                    use_window = len(window_polys) >= min_features
                    if use_window and label_crop_uri is not None:
                        print("Saving test crop labels to {}...".format(label_crop_uri))

                        label_crop_features = [mapping(transform(p2m, window_poly)) for window_poly in window_polys]
                        label_crop_json = {
                            "type": "FeatureCollection",
                            "features": [{"geometry": feature} for feature in label_crop_features],
                        }
                        json_to_file(label_crop_json, label_crop_uri)

                if use_window:
                    save_crop(image_uri, window, image_crop_uri)

                    if not vector_labels and label_uri and label_crop_uri:
                        save_crop(label_uri, window, label_crop_uri)

                    break

            if not use_window:
                raise ValueError("Could not find a good crop.")
        finally:
            os.environ.clear()
            os.environ.update(old_environ)
