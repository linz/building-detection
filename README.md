
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
This initial pipeline focuses on training models to extract buildings from imagery. 
This project is also an opportunity to evaluate Raster Vision for the extraction of 
geo-spatial features from imagery in general.

## Running the Pipeline
The Pipeline can be run either locally or on AWS Batch. But to train a deep 
learning model, you will need access to a decent GPU(s).

### Locally
To train a model, a GPU(s) is required. However during development, local execution 
for testing and debugging is useful. 

#### Setup

* Build the Docker image 

`docker/build`

#### Run

* If using AWS resources (e.g. consuming data from S3), set the AWS_PROFILE 
environment variable. This will be the profile used by the Raster Vision pipeline

`export AWS_PROFILE=<profile name>`

* Execute the `docker/run` script.
If using AWS resources, do so with the `--aws` flag. The `--aws` flag makes the AWS
user configuration available to the container.

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

### AWS Batch
Make use of AWS GPU resources via AWS Batch


#### AWS Batch Resources Deployment 
This repository requires [NodeJs](https://nodejs.org/en/) > 12 & [Yarn](https://yarnpkg.com/en/)

Use [n](https://github.com/tj/n) to manage nodeJs versions

```bash
# Download the latest nodejs & yarn
n latest
npm install -g yarn

# Install node deps
yarn

# Build everything into /build
yarn run build

# Compare the stack with the deployed stack 
npx cdk diff

# Deploy the strack 
npx cdk deploy
```

#### Update Pipeline configuration
After creating the Batch resources, set the following parameters in the
 [.rastervision/batch](https://github.com/linz/building-detection/blob/.rastervision/batch) 
 configuration file. Check the AWS Batch console to see the names of the 
resources that were created, as they can vary. 

* gpu_job_queue - job queue for GPU jobs
* gpu_job_def - job definition that defines the GPU Batch jobs
* cpu_job_queue - job queue for CPU-only jobs
* cpu_job_def - job definition that defines the CPU-only Batch jobs
* attempts - Optional number of attempts to retry failed jobs. It is good to set this to > 1 since Batch often kills jobs for no apparent reason.



#### Run Batch
* Run the Pipeline container. This is easier to access Raster Vision than installing it locally.

`export AWS_PROFILE=<profile name>`

`docker/run --aws`

* Run the RasterVision `batch` command

```
rastervision -p <profile> run batch building_detection/building_detection.py \
    -a raw_uri 's3://<Bucket name where images and labels  are>/' \
    -a processed_uri '<Path to processed data>' \
    -a root_uri '<Path to outputs>'
```

For Example
```
rastervision -p <profile> run batch building_detection/building_detection.py \
    -a raw_uri 's3://rastervisiontest/' \
    -a processed_uri 's3://rastervisiontest/output/data/processed/' \
    -a root_uri 's3://rastervisiontest/output/'
```

or just select commands such as train, predict and eval

```
rastervision -p profile run batch building_detection/building_detection.py \
    train predict eval
    -a raw_uri 's3://rastervisiontest/' \
    -a processed_uri 's3://rastervisiontest/output/data/processed/' \
    -a root_uri 's3://rastervisiontest/output/'
```

## Predict
currently predict can only be executed locally 

Using a trained model run the below

```
rastervision predict <path to model-bundle.zip> \
    <path to image to predict on> \
    <output path for TIFF with predictions> \
    --vector-label-uri <(output path for vectorised predictions)>
```



## Contributing 
See [CONTRIBUTING.md](https://github.com/linz/building-detection/blob/master/CONTRIBUTING.md)
