import cdk = require('@aws-cdk/core');
import iam = require('@aws-cdk/aws-iam');
import batch = require('@aws-cdk/aws-batch');
import ec2 = require('@aws-cdk/aws-ec2');
import ecrAssets = require('@aws-cdk/aws-ecr-assets');
import { join } from "path";

const rasterVision = new cdk.App();

export class RasterVisionStack extends cdk.Stack {
  public constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const batchServiceRole = new iam.Role(this, 'RasterVisionBatchRole', {
      roleName: 'RasterVisionBatchRole',
      assumedBy: new iam.ServicePrincipal('batch.amazonaws.com'),
    });

    batchServiceRole.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSBatchServiceRole'),
    );


    const spotFleetRole = new iam.Role(this, 'RasterVisionSpotFleetRole', {
      roleName: 'RasterVisionSpotFleetRole',
      assumedBy: new iam.ServicePrincipal('spotfleet.amazonaws.com'),
    });
    spotFleetRole.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AmazonEC2SpotFleetTaggingRole'),
    );


    const batchInstanceRole = new iam.Role(this, 'RasterVisionInstanceRole', {
      roleName: 'RasterVisionInstanceRole',
      assumedBy: new iam.CompositePrincipal(
        new iam.ServicePrincipal('ec2.amazonaws.com'),
        new iam.ServicePrincipal('ecs.amazonaws.com'),
      ),
    });
    batchInstanceRole.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AmazonEC2ContainerServiceforEC2Role'),
    );
    batchInstanceRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonS3FullAccess'));
    batchInstanceRole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSSMManagedInstanceCore'));


    // Since roles are passed in via the CLI we ned to assume all the roles
    const stsPolicy = new iam.PolicyStatement();
    stsPolicy.addActions('sts:AssumeRole');
    stsPolicy.addAllResources(); // literally all of the roles!
    batchInstanceRole.addToPolicy(stsPolicy);

    new iam.CfnInstanceProfile(this, 'RasterVisionInstanceProfile', {
      instanceProfileName: batchInstanceRole.roleName,
      roles: [batchInstanceRole.roleName],
    });

    // Container 
    // const image = ContainerImage.fromAsset('./container');
    const container = new ecrAssets.DockerImageAsset(this, 'RasterVisionContainer', {
      directory: './',
      exclude: [
        'node_modules',
        '.git',
        'cdk.out'
      ]
    });


    const vpc = ec2.Vpc.fromLookup(this, 'RasterVisionVpc', { tags: { BaseVPC: 'true' } });
    const sg = new ec2.SecurityGroup(this, 'RasterVisionBatchSecurity', { vpc });

    // Launch Template
    const launchTemplateData = {

      blockDeviceMappings: [
        {
          deviceName: '/dev/xvda',
          ebs: {
            volumeSize: 1000,
            volumeType: 'gp2',
          },
        },

      ],
    };

    const launchTemplateName = `LaunchTemplate`;
    new ec2.CfnLaunchTemplate(this, launchTemplateName, { launchTemplateData, launchTemplateName });


    //////////////////////
    // CPU Resources
    /////////////////////

    // CPU Compute Envi
    const CpuComputeEnv = new batch.CfnComputeEnvironment(this, 'RasterVisionCpuComputeEnvironment', {
      type: 'MANAGED',
      serviceRole: batchServiceRole.roleArn,
      computeResources: {
        type: 'SPOT',
        maxvCpus: 80,
        minvCpus: 0,
        desiredvCpus: 0,
        spotIamFleetRole: spotFleetRole.roleArn,
        instanceRole: batchInstanceRole.roleName,
        instanceTypes: ['r5.large'],
        subnets: vpc.privateSubnets.map((c) => c.subnetId),
        securityGroupIds: [sg.securityGroupId],
        tags: {
          RasterVisionCpuComputeEnvironment: 'true',
        },
        launchTemplate: {
          launchTemplateName,
          version: '$Latest',
        },
      },
    });

    // Cpu Job Definition 
    new batch.CfnJobDefinition(this, 'RasterVisionCustomPyTorchCpuJobDefinition', {
      jobDefinitionName: 'RasterVisionCustomPyTorchCpuJobDefinition',
      type: 'container',
      containerProperties: {
        image: container.imageUri,
        /**
         * 1 cpu = 1024 CpuShares, this allows the container to use as many VCpu's
         * as possible when in use, having more than 1 share means higher priority
         *
         * @see https://docs.docker.com/config/containers/resource_constraints/
         */
        vcpus: 2,
        /**
         * Most containers do not allocate the full 1GB (1024MB) to the container
         * so this should not be a multiple of 1024
         *
         * Eg a instance with 8192MB allocates 7953MB usable
         */
        memory: 12000,
        privileged: true,
        readonlyRootFilesystem: false,
        mountPoints: [
          {
            containerPath: '/opt/data',
            readOnly: false,
            sourceVolume: 'home'
          },
          {
            containerPath: '/dev/shm',
            readOnly: false,
            sourceVolume: 'shm'
          },
          {
            containerPath: '/tmp',
            readOnly: false,
            sourceVolume: 'tmp'
          },
        ],
        volumes: [{
          name: 'home',
          host: { sourcePath: '/home/ec2-user' }
        },
        {
          name: 'shm',
          host: { sourcePath: '/dev/shm' }
        },
        {
          name: 'tmp',
          host: { sourcePath: '/tmp' }
        }
        ],
      },
    });

    // Cpu Job Queue
    new batch.CfnJobQueue(this, 'RasterVisionCpuJobQueue', {
      jobQueueName: 'RasterVisionCpuJobQueue',
      computeEnvironmentOrder: [
        {
          computeEnvironment: CpuComputeEnv.ref,
          order: 1,
        },
      ],
      priority: 1,
    });


    //////////////////////
    // GPU Resources
    //////////////////////

    // GPU Compute Envi
    const GpuComputeEnv = new batch.CfnComputeEnvironment(this, 'RasterVisionGpuComputeEnvironment', {
      type: 'MANAGED',
      serviceRole: batchServiceRole.roleArn,
      computeResources: {
        type: 'SPOT',
        maxvCpus: 80,
        minvCpus: 0,
        desiredvCpus: 0,
        spotIamFleetRole: spotFleetRole.roleArn,
        instanceRole: batchInstanceRole.roleName,
        instanceTypes: ['p3.2xlarge'],
        subnets: vpc.privateSubnets.map((c) => c.subnetId),
        securityGroupIds: [sg.securityGroupId],
        tags: {
          RasterVisionCpuComputeEnvironment: 'true',
        },
        launchTemplate: {
          launchTemplateName,
          version: '$Latest',
        },
      },
    });

    // Gpu Job Definition 
    new batch.CfnJobDefinition(this, 'RasterVisionCustomPyTorchGpuJobDefinition', {
      jobDefinitionName: 'RasterVisionCustomPyTorchGpuJobDefinition',
      type: 'container',
      containerProperties: {
        image: container.imageUri,
        /**
         * 1 cpu = 1024 CpuShares, this allows the container to use as many VCpu's
         * as possible when in use, having more than 1 share means higher priority
         *
         * @see https://docs.docker.com/config/containers/resource_constraints/
         */
        vcpus: 8,
        /**
         * Most containers do not allocate the full 1GB (1024MB) to the container
         * so this should not be a multiple of 1024
         *
         * Eg a instance with 8192MB allocates 7953MB usable
         */
        memory: 12000,
        privileged: true,
        readonlyRootFilesystem: false,
        linuxParameters: {
          sharedMemorySize: 12000
        },
        resourceRequirements: [
          {
            type: 'GPU',
            value: '1'
          }
        ],

        mountPoints: [
          {
            containerPath: '/opt/data',
            readOnly: false,
            sourceVolume: 'home'
          },
          {
            containerPath: '/dev/shm',
            readOnly: false,
            sourceVolume: 'shm'
          },
          {
            containerPath: '/tmp',
            readOnly: false,
            sourceVolume: 'tmp'
          },
        ],
        volumes: [{
          name: 'home',
          host: { sourcePath: '/home/ec2-user' }
        },
        {
          name: 'shm',
          host: { sourcePath: '/dev/shm' }
        },
        {
          name: 'tmp',
          host: { sourcePath: '/tmp' }
        }
        ],
      },
    });

    // Gpu Job Queue
    new batch.CfnJobQueue(this, 'RasterVisionGpuJobQueue', {
      jobQueueName: 'RasterVisionGpuJobQueue',
      computeEnvironmentOrder: [
        {
          computeEnvironment: GpuComputeEnv.ref,
          order: 1,
        },
      ],
      priority: 1,
    });
  }
}

new RasterVisionStack(rasterVision, 'BuildingDetection', { env: { region: 'ap-southeast-2', account: '686418035187' } });
