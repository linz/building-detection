import { ComputeEnvironment, ComputeResourceType, JobDefinition, JobQueue } from '@aws-cdk/aws-batch';
import { Vpc, InstanceType, InstanceSize, InstanceClass } from '@aws-cdk/aws-ec2';
import { App, CfnOutput, Construct, Stack, StackProps } from '@aws-cdk/core';
import { ContainerImage } from '@aws-cdk/aws-ecs';

const rasterVision = new App();

export class RasterVisionStack extends Stack {
  public constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const vpc = Vpc.fromLookup(this, 'RvVpc', { tags: { BaseVPC: 'true' } });

    const computeEnvironment = new ComputeEnvironment(this, 'RvCompute', {
      computeResources: {
        type: ComputeResourceType.SPOT,
        vpc,
        instanceTypes: [InstanceType.of(InstanceClass.R5, InstanceSize.LARGE)],
      },
    });

    const image = ContainerImage.fromAsset('./container');
    const jobDef = new JobDefinition(this, 'RvJobDef', { container: { image, vcpus: 1, memoryLimitMiB: 1024 } });

    const computeEnvironments = [{ computeEnvironment, order: 1 }];
    const jobQueue = new JobQueue(this, 'RvQueue', { computeEnvironments, priority: 1 });

    new CfnOutput(this, 'JobDef', { value: jobDef.jobDefinitionArn });
    new CfnOutput(this, 'JobQueue', { value: jobQueue.jobQueueArn });
  }
}

new RasterVisionStack(rasterVision, 'RasterBatch', { env: { region: 'ap-southeast-2', account: '686418035187' } });
