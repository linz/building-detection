"""
Configuration for building detection pipeline
"""

# TRAIN_IDS = ["BG43_5000_0709"]

# VALID_IDS = ["BG43_5000_0710"]

TRAIN_IDS = ["BG32_5K_0708_TRAIN"]

VALID_IDS = ["BG32_5K_0708_VAL"]

CHIP_SIZE = 300

# NIR-RGB
CHANNEL_ORDER = [1, 2, 3]

# Segmentation Config
NUM_EPOCHS = 50
TEST_NUM_EPOCHS = 1
BATCH_SIZE = 8
LEARNING_RATE = 1e-4
