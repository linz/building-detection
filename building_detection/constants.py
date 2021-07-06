"""
Configuration for building detection pipeline
"""

from data_config import get_training_data

CHIP_SIZE = 300

# NIR-RGB
CHANNEL_ORDER = [0, 1, 2, 3]

# Segmentation Config
NUM_EPOCHS = 7
TEST_NUM_EPOCHS = 4
BATCH_SIZE = 8  # mem error at 32
LEARNING_RATE = 1e-4
DATA = get_training_data()
