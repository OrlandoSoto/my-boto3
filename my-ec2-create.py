#!/usr/bin/env python
# Utility to create a bucket and upload a file to it
import utility
import boto3

my_bucket_name = 'orlando-bucket'



# Boto 3
import boto3
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print instance.id, instance.state

instance = ec2.create_instances(
    ImageId='ami-976152f2',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
print instance[0].id

