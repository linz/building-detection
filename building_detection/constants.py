"""
Configuration for building detection pipeline


rastervision run local building_detection/building_detection.py \
    train predict eval bundle \
    -a raw_uri 's3://building-detection-data/' \
    -a processed_uri '/opt/data/processed/' \
    -a root_uri '/opt/data/output/' \
    -a test True \
    -a multiband False

"""

image_datasets = {"gisborne_2017-2018": {"path": "RGBi2/RBGi_gisborne_0.3m_rural_2017-2018", "file_type": "TIF"}}


# TRAIN_IDS = {
#     "BD45_5K_0609": {
#         "path": image_datasets["gisborne_2017-2018"]["path"],
#         "file_type": image_datasets["gisborne_2017-2018"]["file_type"],
#     },
#     "BD45_5K_0503": {
#         "path": image_datasets["gisborne_2017-2018"]["path"],
#         "file_type": image_datasets["gisborne_2017-2018"]["file_type"],
#     },
# }
# "BD45_5K_0502",
#     "BD45_5K_0503",
#     "BD45_5K_0605",
#     "BD45_5K_1003",
#     "BE43_5K_0910",
#     "BE44_5K_0110",
#     "BE44_5K_0408",
#     "BE44_5K_0610",
#     "BE44_5K_0810",
#     "BE45_5K_0303",
#     "BE45_5K_0403",
#     "BE45_5K_1001",
#     "BF42_5K_0601",
#     "BF42_5K_0701",
#     "BF43_5K_1002",
#     "BF44_5K_0110",
#     "BF44_5K_0808",
#     "BG41_5K_0905",
#     "BG43_5K_0404",
#     "BG43_5K_0503",
#     "BG43_5K_0506",
#     "BG43_5K_0507",
#     "BG43_5K_0606",
#     "BG43_5K_0607",
#     "BG43_5K_0608",
#     "BG43_5K_0708",
#     "BG43_5K_0710",


# VALID_IDS = {
#     "BD45_5K_0701": {
#         "path": image_datasets["gisborne_2017-2018"]["path"],
#         "file_type": "tif",  # this is lower case. most of the dataser is upper :(
#     },
# }
#  "BE44_5K_1010", "BE44_5K_0310", "BD45_5K_0907", "BG43_5K_0709", "BG43_5K_0609"


DATA = {
    "training": {
        "BD45_5K_0609": {
            "path": image_datasets["gisborne_2017-2018"]["path"],
            "file_type": image_datasets["gisborne_2017-2018"]["file_type"],
        },
        "BD45_5K_0503": {
            "path": image_datasets["gisborne_2017-2018"]["path"],
            "file_type": image_datasets["gisborne_2017-2018"]["file_type"],
        },
    },
    "validation": {
        "BD45_5K_0701": {
            "path": image_datasets["gisborne_2017-2018"]["path"],
            "file_type": "tif",  # this is lower case. most of the dataser is upper :(
        }
    },
}

CHIP_SIZE = 300

# NIR-RGB
CHANNEL_ORDER = [0, 1, 2, 3]

# Segmentation Config
NUM_EPOCHS = 1
TEST_NUM_EPOCHS = 3
BATCH_SIZE = 8  # mem error at 32
LEARNING_RATE = 1e-4
