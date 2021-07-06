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


CHIP_SIZE = 300

# NIR-RGB
CHANNEL_ORDER = [0, 1, 2, 3]

# Segmentation Config
NUM_EPOCHS = 3
TEST_NUM_EPOCHS = 4
BATCH_SIZE = 8  # mem error at 32
LEARNING_RATE = 1e-4

# Path configurations
image_datasets = {
    "waikato_rural_2017-19_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/waikato_rural_2017-19_0.3m",
        "file_type": "tif",
    },
    "christchurch_urban_2015-2016": {
        "s3_uri": "s3://linz-data-lake-raster-prod",
        "path": "aerial-imagery/new-zealand/christchurch_urban_2015-2016_0.075m_RGB",
        "file_type": "tif",
    },
}

# Training and validation data
DATA = {
    "training": {
        "BB32_5000_0906": {
            "s3_uri": image_datasets["waikato_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["waikato_rural_2017-19_0.3m"]["path"],
            "file_type": image_datasets["waikato_rural_2017-19_0.3m"]["file_type"],
        },
        "BB32_5000_1007": {
            "s3_uri": image_datasets["waikato_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["waikato_rural_2017-19_0.3m"]["path"],
            "file_type": image_datasets["waikato_rural_2017-19_0.3m"]["file_type"],
        },
        "BW23_500_098097": {
            "s3_uri": image_datasets["christchurch_urban_2015-2016"]["s3_uri"],
            "path": image_datasets["christchurch_urban_2015-2016"]["path"],
            "file_type": image_datasets["christchurch_urban_2015-2016"]["file_type"],
        },
    },
    "validation": {
        "BC33_5000_1005": {
            "s3_uri": image_datasets["waikato_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["waikato_rural_2017-19_0.3m"]["path"],
            "file_type": "tif",  # this is lower case. most of the dataset is upper :(
        }
    },
}
