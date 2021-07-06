"""
Rastervision pipeline for building detection.
Modified for Rastervision 0.13
"""

# pylint disabled for RV imports. RV is intended to be executed in a container
import os
from os.path import join

from constants import BATCH_SIZE, CHIP_SIZE, DATA, LEARNING_RATE, NUM_EPOCHS, TEST_NUM_EPOCHS
from rastervision.core.data import (  # pylint: disable=import-error
    ClassConfig,
    DatasetConfig,
    GeoJSONVectorSourceConfig,
    PolygonVectorOutputConfig,
    RasterioSourceConfig,
    RasterizerConfig,
    SemanticSegmentationLabelSourceConfig,
    SemanticSegmentationLabelStoreConfig,
    StatsTransformerConfig,
)
from rastervision.core.data.raster_source import RasterizedSourceConfig  # pylint: disable=import-error
from rastervision.core.data.scene_config import SceneConfig  # pylint: disable=import-error
from rastervision.core.rv_pipeline import (  # pylint: disable=import-error
    SemanticSegmentationChipOptions,
    SemanticSegmentationConfig,
    SemanticSegmentationWindowMethod,
)
from rastervision.pytorch_backend import PyTorchSemanticSegmentationConfig  # pylint: disable=import-error
from rastervision.pytorch_learner import (  # pylint: disable=import-error
    Backbone,
    GeoDataWindowConfig,
    GeoDataWindowMethod,
    SemanticSegmentationGeoDataConfig,
    SemanticSegmentationModelConfig,
    SolverConfig,
)
from utils.crop_images import crop_image


# pylint: disable=unused-argument:
def get_config(
    runner, labels_uri, processed_uri, root_uri, multiband: bool = False, test=False
):  # pylint: disable=too-many-arguments, too-many-locals
    """
    The get_config function returns an instantiated PipelineConfig
    Arguments are passed from the CLI using the -a option.

    @param runner: The name of the runner used to run the pipeline (local or batch)
    @type runner: str
    @param labels_uri: URI where labels are stored (can be local or s3)
    @type  labels_uri: str
    @param processed_uri: URI of processed images and labels are stored
    @type  processed_uri: str
    @param root_uri: URI to store RasterVision outputs
    @type  root_uri: str
    @param test: If true runs an abbreviated experiment for testing/debugging purposes
    @type  test: bool

    @return: Returns an instantiated PipelineConfig
    @rtype: PipelineConfig
    """

    train_ids = [*DATA["training"]]
    val_ids = [*DATA["validation"]]

    if test:
        train_ids = train_ids[0:1]
        val_ids = val_ids[0:1]

    if multiband:
        # use all 4 channels
        channel_order = [0, 1, 2, 3]
        channel_display_groups = {"RGB": (0, 1, 2), "IR": (3,)}
        # aug_transform = example_multiband_transform
    else:
        # use red, & green, blue channels only
        channel_order = [0, 1, 2]
        channel_display_groups = None
        # aug_transform = example_rgb_transform

    class_config = ClassConfig(names=["building", "background"], colors=["red", "black"])  # TODO MOVE TO CONFIG

    def make_scene(scene_id, data_use):
        """
        Configure images and corresponding lables for training

        @param scene_id: The identifier for the imagery and corresponding labels
        @type  test: str

        @return: returns an instantiated PipelineConfig
        @rtype: rastervision.core.data.scene_config.SceneConfig
        """

        scene_id = scene_id.replace("-", "_")
        data_dict = DATA[data_use][scene_id]
        if data_dict["path"]:
            raster_uri = "{}/{}/{}.{}".format(
                data_dict["s3_uri"], data_dict["path"], scene_id, data_dict["file_type"]
            )  # cross accout
        print(raster_uri)

        label_uri = "{}/labels/{}.geojson".format(labels_uri, scene_id)

        if test:
            crop_uri = join(processed_uri, "crops", os.path.basename(raster_uri))
            label_crop_uri = join(processed_uri, "crops", os.path.basename(label_uri))
            crop_image(raster_uri, crop_uri, label_uri=label_uri, label_crop_uri=label_crop_uri, size=600, vector_labels=True)
            raster_uri = crop_uri
            label_uri = label_crop_uri

        # infrared, red, green
        # channel_order = CHANNEL_ORDER
        raster_source = RasterioSourceConfig(
            uris=[raster_uri], channel_order=channel_order, transformers=[StatsTransformerConfig()]
        )

        # Vector Labels
        vector_source = GeoJSONVectorSourceConfig(uri=label_uri, default_class_id=0, ignore_crs_field=True)

        label_source = SemanticSegmentationLabelSourceConfig(
            raster_source=RasterizedSourceConfig(
                vector_source=vector_source, rasterizer_config=RasterizerConfig(background_class_id=1)
            )
        )

        label_store = SemanticSegmentationLabelStoreConfig(rgb=False, vector_output=[PolygonVectorOutputConfig(class_id=0)])

        scene = SceneConfig(id=scene_id, raster_source=raster_source, label_source=label_source, label_store=label_store)

        return scene

    scene_dataset = DatasetConfig(
        class_config=class_config,
        train_scenes=[make_scene(id, "training") for id in train_ids],
        validation_scenes=[make_scene(id, "validation") for id in val_ids],
    )

    chip_options = SemanticSegmentationChipOptions(window_method=SemanticSegmentationWindowMethod.sliding, stride=CHIP_SIZE)

    window_opts = GeoDataWindowConfig(  # could set per scene
        method=GeoDataWindowMethod.sliding, size=CHIP_SIZE, stride=chip_options.stride
    )

    data = SemanticSegmentationGeoDataConfig(
        scene_dataset=scene_dataset,
        window_opts=window_opts,
        img_sz=CHIP_SIZE,
        img_channels=len(channel_order),
        num_workers=4,
        channel_display_groups=channel_display_groups,
        augmentors=["RandomRotate90", "HorizontalFlip", "VerticalFlip"],
    )

    model = SemanticSegmentationModelConfig(backbone=Backbone.resnet101)

    backend = PyTorchSemanticSegmentationConfig(
        data=data,
        model=model,
        solver=SolverConfig(lr=LEARNING_RATE, num_epochs=NUM_EPOCHS, test_num_epochs=TEST_NUM_EPOCHS, batch_sz=BATCH_SIZE),
        log_tensorboard=True,
        run_tensorboard=False,
        test_mode=test,
    )

    pipeline = SemanticSegmentationConfig(
        root_uri=root_uri, dataset=scene_dataset, backend=backend, train_chip_sz=CHIP_SIZE, predict_chip_sz=CHIP_SIZE
    )
    return pipeline
