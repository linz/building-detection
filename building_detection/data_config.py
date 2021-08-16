"""
Config data
Could be json but VSC is formating the python dict nicer
"""

image_datasets = {
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

DATA_CONFIG = {
    #########################
    ### TRAINING DATA
    #########################
    # Auckland_urban_2017_0.075m
    "training": {
        # Auckland_urban_2017_0.075m
        "BA32_4010": {
            "s3_uri": image_datasets["auckland_urban_2017_0.075m"]["s3_uri"],
            "path": image_datasets["auckland_urban_2017_0.075m"]["path"],
            "file_type": image_datasets["auckland_urban_2017_0.075m"]["file_type"],
        },
        "BA32_4011": {
            "s3_uri": image_datasets["auckland_urban_2017_0.075m"]["s3_uri"],
            "path": image_datasets["auckland_urban_2017_0.075m"]["path"],
            "file_type": image_datasets["auckland_urban_2017_0.075m"]["file_type"],
        },
        "BA32_3911": {
            "s3_uri": image_datasets["auckland_urban_2017_0.075m"]["s3_uri"],
            "path": image_datasets["auckland_urban_2017_0.075m"]["path"],
            "file_type": image_datasets["auckland_urban_2017_0.075m"]["file_type"],
        },
        # Christchurch_urban_2015-2016_0.075m_RGB
        "BX24_500_014012": {
            "s3_uri": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["s3_uri"],
            "path": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["path"],
            "file_type": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["file_type"],
        },
        "BX24_500_014013": {
            "s3_uri": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["s3_uri"],
            "path": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["path"],
            "file_type": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["file_type"],
        },
        "BX24_500_015013": {
            "s3_uri": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["s3_uri"],
            "path": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["path"],
            "file_type": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["file_type"],
        },
        "BX24_500_015012": {  # VALIDATION
            "s3_uri": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["s3_uri"],
            "path": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["path"],
            "file_type": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["file_type"],
        },
        # hawkes-bay_rural_2014-2015_0.30m_RGBA
        "BK39_5000_0104": {
            "s3_uri": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["s3_uri"],
            "path": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["path"],
            "file_type": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["file_type"],
        },
        "BK39_5000_0105": {
            "s3_uri": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["s3_uri"],
            "path": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["path"],
            "file_type": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["file_type"],
        },
        "BK39_5000_0204": {
            "s3_uri": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["s3_uri"],
            "path": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["path"],
            "file_type": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["file_type"],
        },
        "BK39_5000_0205": {  # Validate
            "s3_uri": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["s3_uri"],
            "path": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["path"],
            "file_type": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["file_type"],
        },
        # waikato_rural_2017-19_0.3m
        "BD33_5000_0610": {
            "s3_uri": image_datasets["waikato_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["waikato_rural_2017-19_0.3m"]["path"],
            "file_type": image_datasets["waikato_rural_2017-19_0.3m"]["file_type"],
        },
        "BD33_5000_0710": {
            "s3_uri": image_datasets["waikato_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["waikato_rural_2017-19_0.3m"]["path"],
            "file_type": image_datasets["waikato_rural_2017-19_0.3m"]["file_type"],
        },
        "BD33_5000_0810": {
            "s3_uri": image_datasets["waikato_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["waikato_rural_2017-19_0.3m"]["path"],
            "file_type": image_datasets["waikato_rural_2017-19_0.3m"]["file_type"],
        },
        "BD34_5000_0701": {  # Validate
            "s3_uri": image_datasets["waikato_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["waikato_rural_2017-19_0.3m"]["path"],
            "file_type": image_datasets["waikato_rural_2017-19_0.3m"]["file_type"],
        },
        # otago_rural_2017-19_0.3m
        "2018_CC11_5000_0106": {
            "s3_uri": image_datasets["otago_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["otago_rural_2017-19_0.3m"]["path"],
            "file_type": image_datasets["otago_rural_2017-19_0.3m"]["file_type"],
        },
        "2018_CC11_5000_0107": {
            "s3_uri": image_datasets["otago_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["otago_rural_2017-19_0.3m"]["path"],
            "file_type": image_datasets["otago_rural_2017-19_0.3m"]["file_type"],
        },
        "2018_CB11_5000_1007": {
            "s3_uri": image_datasets["otago_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["otago_rural_2017-19_0.3m"]["path"],
            "file_type": image_datasets["otago_rural_2017-19_0.3m"]["file_type"],
        },
    },
    #########################
    ### VALIDATION DATA
    #########################
    # Auckland_urban_2017_0.075m
    "validation": {
        "BA32_3910": {
            "s3_uri": image_datasets["auckland_urban_2017_0.075m"]["s3_uri"],
            "path": image_datasets["auckland_urban_2017_0.075m"]["path"],
            "file_type": image_datasets["auckland_urban_2017_0.075m"]["file_type"],
            # Christchurch_urban_2015-2016_0.075m_RGB
        },
        "BX24_500_015012": {
            "s3_uri": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["s3_uri"],
            "path": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["path"],
            "file_type": image_datasets["christchurch_urban_2015-2016_0.075m_RGB"]["file_type"],
        },
        # hawkes-bay_rural_2014-2015_0.30m_RGBA
        "BK39_5000_0104": {
            "s3_uri": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["s3_uri"],
            "path": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["path"],
            "file_type": image_datasets["hawkes-bay_rural_2014-2015_0.30m_RGBA"]["file_type"],
        },
        # waikato_rural_2017-19_0.3m
        "BD34_5000_0701": {
            "s3_uri": image_datasets["waikato_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["waikato_rural_2017-19_0.3m"]["path"],
            "file_type": image_datasets["waikato_rural_2017-19_0.3m"]["file_type"],
        },
        # otago_rural_2017-19_0.3m
        "2018_CB11_5000_1006": {
            "s3_uri": image_datasets["otago_rural_2017-19_0.3m"]["s3_uri"],
            "path": image_datasets["otago_rural_2017-19_0.3m"]["path"],
            "file_type": image_datasets["otago_rural_2017-19_0.3m"]["file_type"],
        },
    },
}
