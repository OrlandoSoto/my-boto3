import boto3

def print_s3_buckets():

	# Create an S3 client
	s3 = boto3.client('s3')

	# Call S3 to list current buckets
	response = s3.list_buckets()

	# Get a list of all bucket names from the response
	buckets = [bucket['Name'] for bucket in response['Buckets']]

	# Print out the bucket list
	print("Bucket List: %s" % buckets)

def does_bucket_exist(bucket_name):
	s3 = boto3.resource('s3')
	if(s3.Bucket(bucket_name) in s3.buckets.all()):
		return	True
	else:
		return False