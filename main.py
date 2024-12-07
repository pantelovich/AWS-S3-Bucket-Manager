from s3_manager import S3Manager

if __name__ == "__main__":
    s3_manager = S3Manager()
    s3_manager.create_bucket("test-bucket-example")  # Replace with your desired bucket name
