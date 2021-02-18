
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
The Pipeline can be run either locally or on AWS Batch, but to train a deep 
learning model you will need access to GPUs.

### Locally
To train a model, GPUs are required. However during development, local execution for 
testing and debugging is useful. Least using GPUs for local training it is 
recommended the `test True` argument is provided. 

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
Make us of AWS GPU resources via AWS Batch

#### AWS Batch Setup
In order to setup Batch, your AWS account will need to be configured so that:

* You have admin permissions. It is possible with less permissions but this is 
much less straightforward.
* Have the ability to launch P2 or P3 instances.
* Have the accounts credentials configured as a [named profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) 

#### AWS Batch Resources Deployment 
Batch resources are deployed via Cloudformation 

* In the AWS Cloudformation console, select `Create Stack` > `With new resources (standard)`
* On the next page select `Upload a template file` and upload the [cloudformation/template.yml](https://github.com/linz/building-detection/blob/master/cloudformation/template.yml). Then Select `next`
* On the next page (Specify stack details):
  * Under `Stack name` give the stack a name.
  * Select a `VPC`.
  * Select a `Subnet` within the VPC.
  * Select a `SSH key` Name'. This needs to have been created prior.
  * Select a `Instance Type`. p3.2xlarge is a good starting point for training, though if just 
  validating the setup select p2.xlarge 
  * Provide a ECR `Repository Name (PyTorch)` and `Image Tag`. This ECR repository 
  must not already exist as Cloudformation will create the AWS ECR.
  * The remaining values can be left as defaults and `Next` selected
* Accept the terms at the bottom of the page and select `Create Stack` This will deploy the Batch resources

#### Publish Docker Image to ECR
In the above step we pointed the Cloudformation resources at an ECR repository. The Pipeline image must be push
 to this ECR repository so that it can be used by the AWS Batch jobs.


* Run `./docker/build` in the building_detection root directory to build a local 
copy of the Docker image.

* Create the repo name and image tag environment variable for the `ecr_publish` 
script. 

    i.e `BUILDING_DETECTION_ECR_IMAGE=<ecr_repo_name>:<tag_name>`

* Run ./docker/ecr_publish in the building_detection root directory to publish the
Docker  images to ECR. 

Each time the Pipeline is modified the above steps need to be followed to update the Docker image
that is available to the AWS Batch Jobs.


#### Update Pipeline configuration
After creating the Batch resources, set the following parameters in the
 [.rastervision/batch](https://github.com/linz/building-detection/blob/.rastervision/batch) 
 configuration file. Check the AWS Batch console to see the names of the 
resources that were created, as they vary depending on how CloudFormation was 
configured.

* gpu_job_queue - job queue for GPU jobs
* gpu_job_def - job definition that defines the GPU Batch jobs
* cpu_job_queue - job queue for CPU-only jobs
* cpu_job_def - job definition that defines the CPU-only Batch jobs
* attempts - Optional number of attempts to retry failed jobs. It is good to set this to > 1 since Batch often kills jobs for no apparent reason.



#### Run Batch
* Run the Pipeline container. This is easier to access Raster Vision than installing it locally.

`export AWS_PROFILE=<profile name>`

`docker/run --aws`

* run the RasterVision `batch` command

```
rastervision -p batch run batch building_detection/building_detection.py \
    -a raw_uri 's3://<Bucket name where images and labels  are>/' \
    -a processed_uri '<Path to processed data>' \
    -a root_uri '<Path to outputs>'
```

For Example
```
rastervision -p batch run batch building_detection/building_detection.py \
    -a raw_uri 's3://rastervisiontest/' \
    -a processed_uri 's3://rastervisiontest/output/data/processed/' \
    -a root_uri 's3://rastervisiontest/output/'
```

## Contributing 
See [CONTRIBUTING.md](https://github.com/linz/building-detection/blob/master/CONTRIBUTING.md)
