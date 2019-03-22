# Run from local against AWS
import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-02bcbb802e03574ba',
     MinCount=1,
     MaxCount=2,
     InstanceType='t2.micro',
     KeyName='Orlando',
     SecurityGroupIds=['sg-8ce60ce4', 'sg-eafb1182']
 )
