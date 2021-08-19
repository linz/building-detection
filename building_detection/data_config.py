"""
Config data for training and validation
"""

# Paths to datasets
IMAGE_DATASETS = {
    "auckland_urban_2017_0.075m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/auckland_urban_2017_0.075m",
        "file_type": "tif",
    },
    "waikato_rural_2017-19_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/waikato_rural_2017-19_0.3m",
        "file_type": "tif",
    },
    "hawkes-bay_rural_2014-2015_0.30m_RGBA": {
        "s3_uri": "s3://linz-data-lake-raster-prod",
        "path": "aerial-imagery/new-zealand/hawkes-bay_rural_2014-2015_0.30m_RGBA",
        "file_type": "tif",
    },
    "christchurch_urban_2015-2016_0.075m_RGB": {
        "s3_uri": "s3://linz-data-lake-raster-prod",
        "path": "aerial-imagery/new-zealand/christchurch_urban_2015-2016_0.075m_RGB",
        "file_type": "tif",
    },
    "otago_rural_2017-19_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/otago_rural_2017-19_0.3m",
        "file_type": "tif",
    },
}

# Manage Datasets for training and validation here
TRAINING_DATASETS = {
    "auckland_urban_2017_0.075m": ["BA32_4010", "BA32_4011", "BA32_3911"],
    "christchurch_urban_2015-2016_0.075m_RGB": ["BX24_500_014012", "BX24_500_014013", "BX24_500_015013", "BX24_500_015012"],
    "hawkes-bay_rural_2014-2015_0.30m_RGBA": ["BK39_5000_0104", "BK39_5000_0105", "BK39_5000_0204", "BK39_5000_0205"],
    "waikato_rural_2017-19_0.3m": ["BD33_5000_0610", "BD33_5000_0710", "BD33_5000_0810", "BD34_5000_0701"],
    "otago_rural_2017-19_0.3m": ["2018_CC11_5000_0106", "2018_CC11_5000_0107", "2018_CB11_5000_1007"],
}
VALIDATION_DATASETS = {
    "auckland_urban_2017_0.075m": ["BA32_3910"],
    "christchurch_urban_2015-2016_0.075m_RGB": ["BX24_500_015012"],
    "hawkes-bay_rural_2014-2015_0.30m_RGBA": ["BK39_5000_0104"],
    "waikato_rural_2017-19_0.3m": ["BD34_5000_0701"],
    "otago_rural_2017-19_0.3m": ["2018_CB11_5000_1006"],
}


def get_training_data():
    """
    Return python dict of data and its paths
    """

    train_and_validation_data = {}
    image_id_and_path = {}
    datasets = {"validation": VALIDATION_DATASETS, "training": TRAINING_DATASETS}
    for training_data_type, training_data in datasets.items():
        for imagery_dataset, tile_ids in training_data.items():
            for tile_id in tile_ids:
                image_id_and_path[tile_id] = {
                    "s3_uri": IMAGE_DATASETS[imagery_dataset]["s3_uri"],
                    "path": IMAGE_DATASETS[imagery_dataset]["path"],
                    "file_type": IMAGE_DATASETS[imagery_dataset]["file_type"],
                }
            train_and_validation_data[training_data_type] = image_id_and_path
    return train_and_validation_data
