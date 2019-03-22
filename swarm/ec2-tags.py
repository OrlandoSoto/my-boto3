import boto3
ec2 = boto3.resource('ec2')

ec2.create_tags(
    Resources=['i-05b1ee9d97c91e196'],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'manager-1'
        }
    ]
)

ec2.create_tags(
    Resources=['i-07e8a0d4833daf633'],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'worker-1'
        }
    ]
)