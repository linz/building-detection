# Data Preprocessing
Utilities for preparing training data. 


## create_labels.py
Utility for creating labels from LDS datasets. 

The utility takes a LDS dataset and chunks it into individual geojson files as per the extent of a supplied tile index.

In the context of this project, it allows us to use imagery dataset's tile index to 
split the [nz buildings outlines all sources dataset](https://data.linz.govt.nz/layer/101292-nz-building-outlines-all-sources/)
into individual geojson files for the purposes of "labels"


### Usage
The utility is a CLI program. 

For details on each argument run the below help command

`python create_labels.py --help`

Many of the arguments have default values and their use is only required for rear cases. See the 
[examples](https://github.com/linz/building-detection/tree/create_labels/src/data_preprocessing#examples) section for the most common use cases.


### LDS API Key
The script requires an LDS API KEY. This can be set by the `--lds-api-key` argument, however it is recommended 
that the `LDS_API_KEY` environment variable is set prior to execution and the utility will use this by default. 

The LDS_API_KEY environment variable can be set prior to the execution of the utility as below

`export LDS_API_KEY=<YOUR LDS KEY>`

### AWS Profile
If writing the labels to s3, a [named AWS profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)
must be provided via the `--aws-profile` argument.

### Examples
There are two different usages that require different arguments to be provided:
1. Writing the labels locally
2. Writing the labels to s3

#### Create and write labels locally 

```
python /create_labels.py \
    --output-path <path_to_write_labels_to> \
    --lds-tile-layer <the lds tile index dataset being used to chunk labels > \
    --lds-tile-id-field <the above dataset's attribute field that refers to the tile id> \
    --building-source-imagery <The name of the imagery dataset that the buildings of interest have been extracted from> \
    --tile-id "BQ31_5000_0610" \
    --tile-id "BQ31_5000_0509" \
    --tile-id "BQ31_5000_0608" \
    --tile-id "BQ31_5000_0508"
```

##### Real world example
The below creates labels for the "Auckland 0.075m Urban Aerial Photos (2017)" imagery dataset



```
python3 create_labels.py \
--output-path "~/projects/deep_learning_project/labels" \
--lds-tile-layer 95439 \
--lds-tile-id-field TILENAME \
--building-source-imagery "Auckland 0.075m Urban Aerial Photos (2017)
--tile-id BA31_1k_2333 \

```

Where:
* `--lds-tile-layer 95439` refers to the [tile index dataset](https://data.linz.govt.nz/layer/95439-auckland-0075m-urban-aerial-photos-index-tiles-2017/)
 we want to split the [buildings outlines dataset](https://data.linz.govt.nz/layer/101292-nz-building-outlines-all-sources/) by into  individual label files. This should be the index tile dataset 
 as related to the imagery dataset the labels are being created for. 
* `--lds-tile-id-field TILENAME` "TILENAME" is the name of the attribute field that refers to each tile's id. Providing this field's name allows 
querying of the dataset to return the properties of the tiles of interested. 
* `--building-source-imagery "Auckland 0.075m Urban Aerial Photos (2017)"` By providing an imagery source it is ensured that only the building 
outlines as related to the imagery for training is extracted to the label file. This solves the problem when within the tile's extent exist buildings 
of different epochs as related to different aerial surveys.
* `--tile-id` The id of the tile we want labels/buildings extracted for it's extent into a label file. 

#### Create and write labels to S3 
The bellow performs the same tiling operation as above but outputs the labels to s3. 

```
export LDS_API_KEY=<YOUR LDS KEY>

python /create_labels.py \
    --store-type s3 \
    --aws-profile <named aws profile> \
    --output-path <path_to_write_labels_to> \
    --lds-tile-layer <the lds tile dataset being used to chunk labels > \
    --lds-tile-id-field <the above datasets attribute field that refs to the tile id> \
    --building-source-imagery <The name of the imagery dataset that the buildings of interest have been extracted from> \
    --tile-id "BQ31_5000_0610" \
    --tile-id "BQ31_5000_0509" \
    --tile-id "BQ31_5000_0608" \
    --tile-id "BQ31_5000_0508"
```


python3 create_labels.py \
--output-path "~/projects/deep_learning_project/labels" \
--lds-tile-layer 95439 \
--lds-tile-id-field TILENAME \
--building-source-imagery "Auckland 0.075m Urban Aerial Photos (2017)
--tile-id BA31_1k_2333 \