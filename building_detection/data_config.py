"""
Config data for training and validation
"""

# Paths to datasets
IMAGE_DATASETS = {
    # Training & Validation datasets
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
    # Test datasets
    "bay-of-plenty_urban_2014-15_0.125m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/bay-of-plenty_urban_2014-15_0.125m",
        "file_type": "tif",
    },
    "marlborough_rural_2015-2016_0.20m_RGBA": {
        "s3_uri": "s3://linz-data-lake-raster-prod",
        "path": "aerial-imagery/new-zealand/marlborough_rural_2015-2016_0.20m_RGBA",
        "file_type": "tif",
    },
    "waimakariri_urban_2015-2016_0.075m_RGBA": {
        "s3_uri": "s3://linz-data-lake-raster-prod",
        "path": "aerial-imagery/new-zealand/waimakariri_urban_2015-2016_0.075m_RGBA",
        "file_type": "tif",
    },
    "taranaki_rural_2016-17_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/taranaki_rural_2016-17_0.3m",
        "file_type": "tif",
    },
    "dunedin_urban_2018-19_0.1m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/dunedin_urban_2018-19_0.1m",
        "file_type": "tif",
    },
    "gisborne_rural_2017-18_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/gisborne_rural_2017-18_0.3m",
        "file_type": "TIF",
    },
    "canterbury_rural_2016-18_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/canterbury_rural_2016-18_0.3m",
        "file_type": "tif",
    },
    "nelson_rural_2018-19_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/nelson_rural_2018-19_0.3m",
        "file_type": "tif",
    },
    #
    "west-coast_rural_2015-16_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/west-coast_rural_2015-16_0.3m",
        "file_type": "tif",
    },
    "tasman_rural_2016-17_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/tasman_rural_2016-17_0.3m",
        "file_type": "tif",
    },
    "bay-of-plenty_rural_2016-17_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/bay-of-plenty_rural_2016-17_0.3m",
        "file_type": "tif",
    },
    "bay-of-plenty_rural_2015-17_0.25m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/bay-of-plenty_rural_2015-17_0.25m",
        "file_type": "tif",
    },
    "marlborough_rural_2017-18_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/marlborough_rural_2017-18_0.3m",
        "file_type": "tif",
    },
    "west-coast_rural_2016-17_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/west-coast_rural_2016-17_0.3m",
        "file_type": "tif",
    },
    "canterbury_rural_2014-2015_0.30m_RGBA": {
        "s3_uri": "s3://linz-data-lake-raster-prod",
        "path": "aerial-imagery/new-zealand/canterbury_rural_2014-2015_0.30m_RGBA",
        "file_type": "tif",
    },
    "wellington_rural_2016-17_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/wellington_rural_2016-17_0.3m",
        "file_type": "tif",
    },
    "tasman_rural_2018-19_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/tasman_rural_2018-19_0.3m",
        "file_type": "tif",
    },
    "canterbury_rural_2015-2016_0.30m_RGBA": {
        "s3_uri": "s3://linz-data-lake-raster-prod",
        "path": "aerial-imagery/new-zealand/canterbury_rural_2015-2016_0.30m_RGBA",
        "file_type": "tif",
    },
    "manawatu-whanganui_rural_2015-16_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/manawatu-whanganui_rural_2015-16_0.3m",
        "file_type": "tif",
    },
    "manawatu-whanganui_rural_2016-17_0.3m": {
        "s3_uri": "s3://linz-raster-data-store",
        "path": "aerial-imagery/manawatu-whanganui_rural_2016-17_0.3m",
        "file_type": "tif",
    },
}
# Manage Datasets for training and validation here
TRAINING_DATASETS = {
    "auckland_urban_2017_0.075m": [
        "BA31_3609",
        "BA31_3610",
        "BA31_3611",
        "BA31_3612",
        "BA31_3613",
        "BA31_3709",
        "BA31_3710",
        "BA31_3711",
        "BA31_3712",
        "BA31_3713",
        "BA30_4243",
        "BA31_3648",
        "BA31_3649",
        "BA32_3802",
        "BA32_3803",
        "BA31_3548",
    ],
    "christchurch_urban_2015-2016_0.075m_RGB": [
        "BX23_500_020084",
        "BX23_500_021084",
        "BX23_500_022084",
        "BX23_500_023084",
        "BX23_500_024084",
        "BX23_500_020083",
        "BX23_500_021083",
        "BX23_500_022083",
        "BX23_500_023083",
        "BX23_500_024083",
        "BX23_500_020082",
        "BX23_500_021082",
        "BX23_500_022082",
        "BX23_500_023082",
        "BX23_500_024082",
        "BX23_500_020081",
        "BX23_500_021081",
        "BX23_500_022081",
        "BX23_500_023081",
        "BX23_500_024081",
        "BX24_500_021017",
        "BX24_500_022017",
        "BX24_500_021016",
        "BX24_500_022016",
        "BX24_500_021015",
        "BX24_500_022015",
        "BX24_500_021014",
        "BX24_500_022014",
        "BX24_500_021013",
        "BX24_500_022013",
        "BX24_500_033007",
        "BX24_500_034007",
    ],
    "hawkes-bay_rural_2014-2015_0.30m_RGBA": ["BK39_5000_0203", "BK39_5000_0204", "BL37_5000_0307", "BL37_5000_0308"],
    "waikato_rural_2017-19_0.3m": [
        "BJ34_5000_0208",
        "BJ34_5000_0207",
        "BD33_5000_0509",
        "BD33_5000_0609",
        "BD34_5000_0701",
        "BD34_5000_0808",
    ],
    "otago_rural_2017-19_0.3m": ["2018_CA13_5000_1003", "2018_CB11_5000_1006", "2018_CB11_5000_1007"],
    "taranaki_rural_2016-17_0.3m": ["BH29_2K_1406", "BH29_2K_2121"],  #  Added at  epoch31
    "gisborne_rural_2017-18_0.3m": ["BG43_5K_0608"],  #  Added at  epoch31
    "canterbury_rural_2014-2015_0.30m_RGBA": ["BU25_5000_0607", "BU24_5000_0209"],  #  Added at  epoch31
    "tasman_rural_2016-17_0.3m": ["RGB_BR24_5K_1010", "RGB_BR25_5K_0902"],  # Added at epoch 51
    "canterbury_rural_2016-18_0.3m": ["RGB_BW20_5K_1006", "RGB_BX20_5K_0902"],  # Added at epoch 51
    "bay-of-plenty_rural_2015-17_0.25m": ["BE37_2K_2318"],  # Added at epoch 51
    "tasman_rural_2018-19_0.3m": ["2019_BP25_5000_0606"],  # Added at epoch 51
}
VALIDATION_DATASETS = {
    "auckland_urban_2017_0.075m": ["BA31_3549", "BA32_3902", "BA32_3903"],
    "christchurch_urban_2015-2016_0.075m_RGB": [
        "BX24_500_033006",
        "BX24_500_034006",
        "BX24_500_033005",
        "BX24_500_034005",
        "BX24_500_033004",
        "BX24_500_034004",
        "BX24_500_033003",
        "BX24_500_034003",
    ],
    "hawkes-bay_rural_2014-2015_0.30m_RGBA": ["BL37_5000_0705", "BL38_5000_0601"],
    "waikato_rural_2017-19_0.3m": ["BD34_5000_0809", "BD34_5000_0810", "BD35_5000_0801"],
    "otago_rural_2017-19_0.3m": ["2018_CB12_5000_0108", "2018_CC11_5000_0107"],
    "taranaki_rural_2016-17_0.3m": ["BJ30_2K_2502"],  # Added at epoch 31
    "gisborne_rural_2017-18_0.3m": ["BG43_5K_0709"],  # Added at epoch 31
    "canterbury_rural_2014-2015_0.30m_RGBA": ["BW24_5000_0206", "BU26_5000_0101"],  # Added at epoch 31
    "tasman_rural_2016-17_0.3m": ["RGB_BR25_5K_0903"],  # Added at epoch 51
    "canterbury_rural_2016-18_0.3m": ["RGB_BX20_5K_0610"],  # Added at epoch 51
    "bay-of-plenty_rural_2015-17_0.25m": ["BE37_2K_2422"],  # Added at poc h51
}
# Test datasets (holdout datasets)
# VALIDATION_DATASETS = {
#     "bay-of-plenty_urban_2014-15_0.125m": [
#         "2015_BE40_1000_1704_RGB",
#         "2015_BD37_1000_1413_RGB",
#         "2015_BD37_1000_2007_RGB",
#         "2015_BD36_1000_2645_RGB",
#         "2015_BD38_1000_3310_RGB",
#         "2015_BD38_1000_3316_RGB",
#     ],
#     "marlborough_rural_2015-2016_0.20m_RGBA": [
#         "BR28_2000_0221",
#         "BR28_2000_0320",
#         "BR28_2000_0321",
#         "BR27_2000_0610",
#         "BR25_2000_2207",
#     ],
#     "waimakariri_urban_2015-2016_0.075m_RGBA": [
#         "BW24_500_062046",
#         "BW24_500_062047",
#         "BW23_500_080091",
#         "BW23_500_080092",
#         "BW24_500_059009",
#         "BW24_500_059010",
#         "BW24_500_058009",
#         "BW24_500_058010",
#         "BW24_500_057010",
#         "BW24_500_049016",
#     ],
#     "taranaki_rural_2016-17_0.3m": [
#         "BH29_2K_1017",
#         "BH29_2K_1117",
#         "BH29_2K_1214",
#         "BH29_2K_1213",
#         "BH29_2K_1310",
#         "BH29_2K_1309",
#         "BH29_2K_1509",
#         "BH29_2K_1610",
#         "BH29_2K_1611",
#     ],
#     "dunedin_urban_2018-19_0.1m": [
#         "2018_CE16_1000_3046",
#         "2018_CE16_1000_3146",
#         "2018_CE17_1000_3121",
#         "2018_CE17_1000_3120",
#         "2018_CE17_1000_3323",
#         "2018_CE16_1000_2641",
#         "2018_CE16_1000_2642",
#     ],
#     "gisborne_rural_2017-18_0.3m": ["BG43_5K_0607", "BD45_5K_0701", "BG43_5K_0506", "BG43_5K_0308"],
#     "canterbury_rural_2016-18_0.3m": [
#         "RGB_BY17_5K_0901",
#         "RGB_BZ15_5K_0709",
#         "RGB_BY21_5K_0504",
#         "RGB_BY21_5K_0505",
#         "RGB_BX20_5K_0710",
#         "RGB_BX20_5K_0206",
#         "RGB_BZ19_5K_1007",
#     ],
#     "nelson_rural_2018-19_0.3m": ["2019_BQ26_5000_0504", "2019_BQ26_5000_0407", "2019_BQ26_5000_0110"],
#     # More test data - Selected by Jan and Simon
#     "auckland_urban_2017_0.075m": ["BA31_2333", "BA32_5025", "BA32_4732",
#     "BA31_3117", "BB30_0650", "BB31_0802", "BA32_1301"],
#     "christchurch_urban_2015-2016_0.075m_RGB": [
#         "BX24_500_060032",
#         "BX24_500_059032",
#         "BX24_500_060031",
#         "BX24_500_059031",
#         "BX24_500_010050",
#         "BX24_500_011050",
#         "BX24_500_011051",
#         "BX24_500_010051",
#         "BX24_500_028034",
#         "BX24_500_029034",
#         "BX24_500_029035",
#         "BX24_500_028035",
#     ],
#     "hawkes-bay_rural_2014-2015_0.30m_RGBA": ["BL38_5000_0403"],  # rename
#     "waikato_rural_2017-19_0.3m": ["BD34_5000_0903", "BD34_5000_1006"],
#     "otago_rural_2017-19_0.3m": ["2018_CA13_5000_1003", "2018_CC11_5000_0205"],
#     "west-coast_rural_2015-16_0.3m": ["2016_BR20_5000_0909", "2016_BR20_5000_0907", "2016_BU19_5000_0104"],
#     "tasman_rural_2016-17_0.3m": ["RGB_BQ24_5K_0709", "RGB_BR23_5K_1002"],
#     "bay-of-plenty_rural_2016-17_0.3m": ["BD37_5K_0807"],
#     "bay-of-plenty_rural_2015-17_0.25m": ["BE37_2K_1907", "BE37_2K_2109", "BE37_2K_2010", "BF38_2K_1712"],
#     # "marlborough_rural_2017-18_0.3m": [
#     #     "2018_BQ27_2000_1419",
#     #     "2018_BQ28_2000_1025",
#     #     "2018_BQ28_2000_0905",
#     #     "2018_BQ28_2000_0817",
#     # ],
#     "west-coast_rural_2016-17_0.3m": ["2017_BU18_5000_0907"],
#     "canterbury_rural_2014-2015_0.30m_RGBA": ["BU24_5000_0210", "BV24_5000_0605"],
#     "wellington_rural_2016-17_0.3m": ["BQ34_5K_0301"],
#     "tasman_rural_2018-19_0.3m": ["2019_BP24_5000_0109", "2019_BQ26_5000_0602"],
#     "canterbury_rural_2015-2016_0.30m_RGBA": ["BW22_5000_0608", "BX22_5000_0201", "BX23_5000_1002"],
#     "manawatu-whanganui_rural_2015-16_0.3m": ["2016_5000_BM34_0608", "2016_5000_BN33_0203"],
#     "manawatu-whanganui_rural_2016-17_0.3m": ["2017_5k_BH33_0108", "2017_5k_BG33_0806"],
# }


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
