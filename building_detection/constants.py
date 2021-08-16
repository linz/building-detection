"""
Configuration for building detection pipeline

USAGE:
rastervision -p batch run batch building_detection/building_detection.py \
    train predict eval bundle \
    -a labels_uri 's3://building-detection-data' \
    -a processed_uri 's3://building-detection-data/output/data/processed' \
    -a root_uri 's3://building-detection-data/output'\
    -a multiband False
"""
from data_config import DATA_CONFIG

CHIP_SIZE = 300

# NIR-RGB
CHANNEL_ORDER = [0, 1, 2, 3]

# Segmentation Config
NUM_EPOCHS = 5
TEST_NUM_EPOCHS = 4
BATCH_SIZE = 8  # mem error at 32
LEARNING_RATE = 1e-4
DATA = DATA_CONFIG
