import utility
import boto3

my_bucket_name = 'orlando-bucket'
my_bucket_config = {'LocationConstraint': 'us-east-2'}
upload_filename = 'uploads/sample.txt'

# List all buckets by name
utility.print_s3_buckets()

# Create an S3 client
s3 = boto3.client('s3')

# check if the bucket already exists before creating a bucket
if(utility.does_bucket_exist(my_bucket_name)):
    print(my_bucket_name + ' Already exists')
    print('Skipping bucket creation')
else:
    # Create new bucket
    print('Creating bucket: ' + my_bucket_name)
    s3.create_bucket(Bucket=my_bucket_name, CreateBucketConfiguration=my_bucket_config)

# check if the bucket already exists before uploading a file
if(utility.does_bucket_exist(my_bucket_name)):
    s3.upload_file(upload_filename, my_bucket_name, upload_filename)
    print(upload_filename + ' uploaded to ' + my_bucket_name)
else:
    print(my_bucket_name + ' Does NOT exist')

# Print the contents of all buckets
print('Bucket contents: ')
utility.print_all_bucket_contents()