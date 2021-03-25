"""
Rastervision pipeline for building detection
"""

# pylint disabled for RV imports. RV is intended to be executed in a container
import os
from os.path import join

from constants import BATCH_SIZE, CHANNEL_ORDER, CHIP_SIZE, LEARNING_RATE, NUM_EPOCHS, TEST_NUM_EPOCHS, TRAIN_IDS, VALID_IDS
from rastervision.core.data import (  # pylint: disable=import-error
    ClassConfig,
    DatasetConfig,
    GeoJSONVectorSourceConfig,
    PolygonVectorOutputConfig,
    RasterioSourceConfig,
    RasterizerConfig,
    SemanticSegmentationLabelSourceConfig,
    SemanticSegmentationLabelStoreConfig,
)
from rastervision.core.data.raster_source import RasterizedSourceConfig  # pylint: disable=import-error
from rastervision.core.data.scene_config import SceneConfig  # pylint: disable=import-error
from rastervision.core.rv_pipeline import (  # pylint: disable=import-error
    SemanticSegmentationChipOptions,
    SemanticSegmentationConfig,
)
from rastervision.core.rv_pipeline.semantic_segmentation_config import (  # pylint: disable=import-error
    SemanticSegmentationWindowMethod,
)
from rastervision.pytorch_backend import PyTorchSemanticSegmentationConfig  # pylint: disable=import-error
from rastervision.pytorch_learner import (  # pylint: disable=import-error
    Backbone,
    SemanticSegmentationModelConfig,
    SolverConfig,
)
from utils.crop_images import crop_image


# pylint: disable=unused-argument:
def get_config(runner, raw_uri, processed_uri, root_uri, test=False):
    """
    The get_config function returns an instantiated PipelineConfig
    Arguments are passed from the CLI using the -a option.

    @param runner: The name of the runner used to run the pipeline (local or batch)
    @type runner: str
    @param raw_uri: URI where raw images and labels are stored (can be local or s3)
    @type  raw_uri: str
    @param processed_uri: URI of processed images and labels are stored
    @type  processed_uri: str
    @param root_uri: URI to store RasterVision outputs
    @type  root_uri: str
    @param test: If true runs an abbreviated experiment for testing/debugging purposes
    @type  test: bool

    @return: Returns an instantiated PipelineConfig
    @rtype: PipelineConfig
    """

    train_ids = TRAIN_IDS
    val_ids = VALID_IDS

    if test:
        train_ids = train_ids[0:1]
        val_ids = val_ids[0:1]

    class_config = ClassConfig(names=["building", "background"], colors=["red", "black"])

    def make_scene(scene_id):
        """
        Configure images and corresponding lables for training

        @param scene_id: The identifier for the imagery and corresponding labels
        @type  test: str

        @return: returns an instantiated PipelineConfig
        @rtype: rastervision.core.data.scene_config.SceneConfig
        """

        scene_id = scene_id.replace("-", "_")
        raster_uri = "{}images/{}.tif".format(raw_uri, scene_id)
        label_uri = "{}labels/{}.geojson".format(raw_uri, scene_id)

        if test:
            crop_uri = join(processed_uri, "crops", os.path.basename(raster_uri))
            label_crop_uri = join(processed_uri, "crops", os.path.basename(label_uri))
            crop_image(raster_uri, crop_uri, label_uri=label_uri, label_crop_uri=label_crop_uri, size=600, vector_labels=True)
            raster_uri = crop_uri
            label_uri = label_crop_uri

        # infrared, red, green
        channel_order = CHANNEL_ORDER
        raster_source = RasterioSourceConfig(uris=[raster_uri], channel_order=channel_order)

        # Vector Labels
        vector_source = GeoJSONVectorSourceConfig(uri=label_uri, default_class_id=0, ignore_crs_field=True)

        label_source = SemanticSegmentationLabelSourceConfig(
            raster_source=RasterizedSourceConfig(
                vector_source=vector_source, rasterizer_config=RasterizerConfig(background_class_id=1)
            )
        )

        # URI will be injected by scene config.
        # Using rgb=False because we want prediction TIFFs to be in
        # NIR-R-G format.
        label_store = SemanticSegmentationLabelStoreConfig(rgb=False, vector_output=[PolygonVectorOutputConfig(class_id=0)])

        scene = SceneConfig(id=scene_id, raster_source=raster_source, label_source=label_source, label_store=label_store)

        return scene

    dataset = DatasetConfig(
        class_config=class_config,
        train_scenes=[make_scene(id) for id in train_ids],
        validation_scenes=[make_scene(id) for id in val_ids],
    )

    chip_size = CHIP_SIZE

    chip_options = SemanticSegmentationChipOptions(window_method=SemanticSegmentationWindowMethod.sliding, stride=chip_size)

    backend = PyTorchSemanticSegmentationConfig(
        model=SemanticSegmentationModelConfig(backbone=Backbone.resnet101),
        solver=SolverConfig(
            lr=LEARNING_RATE, num_epochs=NUM_EPOCHS, test_num_epochs=TEST_NUM_EPOCHS, batch_sz=BATCH_SIZE, one_cycle=True
        ),
        log_tensorboard=True,
        run_tensorboard=False,
        test_mode=test,
    )

    return SemanticSegmentationConfig(
        root_uri=root_uri,
        dataset=dataset,
        backend=backend,
        train_chip_sz=chip_size,
        predict_chip_sz=chip_size,
        chip_options=chip_options,
    )
