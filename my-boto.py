import utility
import boto3

my_bucket_name = 'orlando-bucket'

# List all buckets by name
utility.print_s3_buckets()

# Create an S3 client
s3 = boto3.client('s3')

# check if the bucket already exists before creating a bucket
if(utility.does_bucket_exist(my_bucket_name)):
	print(my_bucket_name + ' Already exists')
else:
	# Create new bucket 
	print('Creating bucket: ' + my_bucket_name) 
	s3.create_bucket(Bucket=my_bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})


