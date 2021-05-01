
import boto3

# Create bucket

s3 = boto3.resource('s3')
bucket_name="s3pscript1"
try:
    response=s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint':'ap-south-1'})
    print(response)
except Exception as error:
    print(error)
