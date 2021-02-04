
# Building Detection
![](https://img.shields.io/badge/WIP-Work%20In%20Progress-orange)
[![GitHub Actions Status](https://github.com/linz/building-detection/workflows/Build/badge.svg)](https://github.com/linz/building-detection/actions)
[![Kodiak](https://badgen.net/badge/Kodiak/enabled?labelColor=2e3a44&color=F39938)](https://kodiakhq.com/)
[![Dependabot Status](https://badgen.net/badge/Dependabot/enabled?labelColor=2e3a44&color=blue)](https://github.com/linz/building-detection/network/updates)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/linz/building-detection/blob/master/LICENSE)
[![Conventional Commits](https://badgen.net/badge/Commits/conventional?labelColor=2e3a44&color=EC5772)](https://conventionalcommits.org)
[![Code Style](https://badgen.net/badge/Code%20Style/black?labelColor=2e3a44&color=000000)](https://github.com/psf/black)

Pipeline for training computer vision models based on [Raster Vision](https://github.com/azavea/raster-vision).

## Purpose
This initial pipeline focuses on training models to extract buildings from imagery. This project is also an opportunity 
to evaluate Raster Vision for the extraction of geo-spatial features from imagery in general and can be expanded to other feature types.

## Running locally

### Setup

* Build the Docker image 

`docker/build`

### Run

* If using AWS resources, set the AWS_PROFILE environment variable. 
This will be the profile used by the rastervision pipeline

`export AWS_PROFILE=<profile name>`

* Execute the `docker/run` script.
If using AWS resources do so with the `--aws` flag. The `--aws` flag makes the AWS user configuration 
available to the container

`docker/run --aws`

* In the container execute `rastervision run` as below. 
If `-a test True`, the pipeline will select one image and crop it for a 
test run. This allows for quick validation of the pipeline for debugging and
development purposes. 

```
rastervision run local building_detection/building_detection.py \
    -a raw_uri 's3://<bucketname>/' or <local path> \
    -a processed_uri '/opt/data/processed/' \
    -a root_uri '/opt/data/output/' \
    -a test True
```

## Contributing 
See [CONTRIBUTING.md](https://github.com/linz/building-detection/blob/master/CONTRIBUTING.md)
