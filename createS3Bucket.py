# Creating S3 Bucket

import uuid         #to randomize name
import boto3

from AWS_S3_Resource import s3_resource


def create_bucket_name(bucket_prefix):
    #The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])


def createBucket(bucket_prefix, s3_connection):
    session = boto3.Session(profile_name='research')       #creating a session
    s3 = session.client('s3')       #s3 variable -- refer to boto3 api documentation
    bucket_name = create_bucket_name(bucket_prefix)
    #print(bucket_name, current_region)
    bucket_response = s3.create_bucket(   #s3.create_bucket() is part of the s3 API (Refer to S3 boto3 documentation)
        Bucket=bucket_name)
    print(bucket_name, "us-east-1")
    return bucket_name, bucket_response


def main():
    first_bucket_name, first_response = createBucket(
        bucket_prefix='zubair-python-bucket',
        s3_connection=s3_resource.meta.client)


main()