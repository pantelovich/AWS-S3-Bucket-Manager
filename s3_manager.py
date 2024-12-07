import boto3
from botocore.exceptions import ClientError

class S3Manager:
    def __init__(self):
        self.s3 = boto3.client('s3')

    def create_bucket(self, bucket_name):
        try:
            self.s3.create_bucket(Bucket=bucket_name)
            print(f"Bucket {bucket_name} created successfully.")
        except ClientError as e:
            print(f"Error creating bucket: {e}")

    def delete_bucket(self, bucket_name):
        try:
            self.s3.delete_bucket(Bucket=bucket_name)
            print(f"Bucket {bucket_name} deleted successfully.")
        except ClientError as e:
            print(f"Error deleting bucket: {e}")

    def upload_file(self, bucket_name, file_name):
        try:
            self.s3.upload_file(file_name, bucket_name, file_name)
            print(f"File {file_name} uploaded to {bucket_name}.")
        except ClientError as e:
            print(f"Error uploading file: {e}")
