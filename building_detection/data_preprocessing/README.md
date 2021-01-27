# Data Preprocessing
Utilities for preparing training data. 


## create_labels.py
Utility for creating labels from LDS datasets. 

The utility takes a LDS dataset and chunks it into individual geojson files as per the extent of the supplied ([nz-5k-tile-index](https://data.linz.govt.nz/layer/104691-nz-15k-tile-index/) by default) index tile.

In the context of this project, it allows us to use the [nz-5k-tile-index](https://data.linz.govt.nz/layer/104691-nz-15k-tile-index/) to 
tile the [nz buildings dataset](https://data.linz.govt.nz/layer/101290-nz-building-outlines/) into individual tiles that match the 5k index,
the same index aerial photos are tiled to.


### Usage
The utility is a CLI program. 

For details on each argument run the below help command

`python create_labels.py --help`

Many of the arguments have default values and are only required for advanced use. See the 
[examples](https://github.com/linz/building-detection/tree/create_labels/src/data_preprocessing#examples) section
for the most common use cases.


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
The below example tiles the default dataset ([nz building outlines](https://data.linz.govt.nz/layer/101290-nz-building-outlines/))
by the default tile index (([nz-15k-tile-index](https://data.linz.govt.nz/layer/104691-nz-15k-tile-index/)) for the supplied tiles
and writes them locally. 

```
python /create_labels.py \
    --output-path <path_to_write_labels_to> \
    --tile-id "BQ31_5000_0610" \
    --tile-id "BQ31_5000_0509" \
    --tile-id "BQ31_5000_0608" \
    --tile-id "BQ31_5000_0508"
```

#### Create and write labels to S3 
The bellow performs the same tiling operation as above but outputs the labels to s3. 

```
export LDS_API_KEY=<YOUR LDS KEY>

python /create_labels.py \
    --store-type s3 \
    --aws-profile <named aws profile> \
    --output-path <s3 bucket name> \
    --tile-id "BQ31_5000_0610" \
    --tile-id "BQ31_5000_0509" \
    --tile-id "BQ31_5000_0608" \
    --tile-id "BQ31_5000_0508"
```