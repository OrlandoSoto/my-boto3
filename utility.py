import boto3


def print_s3_buckets():

    # Create an S3 resource
    s3 = boto3.resource('s3')

    # Print out the bucket list
    for bucket in s3.buckets.all():
        print('Bucket name: ' + bucket.name)




def does_bucket_exist(bucket_name):
    # Create an S3 resource
    s3 = boto3.resource('s3')

    # Check if the bucket name exists
    if(s3.Bucket(bucket_name) in s3.buckets.all()):
        return True
    else:
        return False


def print_all_bucket_contents():
    # Create an S3 resource
    s3 = boto3.resource('s3')

    for bucket in s3.buckets.all():
        for key in bucket.objects.all():
            print(key.key)