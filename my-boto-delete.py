#!/usr/bin/env python
# Utility to delete a bucket
import utility
import boto3

my_bucket_name = 'orlando-bucket'
my_bucket_config = {'LocationConstraint': 'us-east-2'}
upload_filename = 'uploads'

# List all buckets by name
utility.print_s3_buckets()

# Create an S3 client
s3 = boto3.resource('s3')
bucket = s3.Bucket(my_bucket_name)

# Print the contents of all buckets
print('Bucket contents: ')
utility.print_all_bucket_contents()

# Empty the bucket before deletion
bucket.objects.all().delete()

# check if the bucket already exists before deleting a bucket
if(utility.does_bucket_exist(my_bucket_name)):
    bucket.delete()
    # Print confirmation
    print(my_bucket_name + ' Successfully deleted')
else:
    # No bucket to delete
    print(my_bucket_name + ' Already exists')
    print('Skipping bucket creation')
