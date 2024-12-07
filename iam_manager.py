import boto3
from botocore.exceptions import ClientError

class IAMManager:
    def __init__(self):
        self.iam = boto3.client('iam')

    def apply_policy(self, bucket_name, policy_name):
        try:
            # Assuming a basic bucket policy is applied
            policy = {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": "s3:*",
                        "Resource": f"arn:aws:s3:::{bucket_name}/*"
                    }
                ]
            }

            self.iam.put_bucket_policy(
                Bucket=bucket_name,
                Policy=str(policy)
            )
            print(f"Policy {policy_name} applied to bucket {bucket_name}.")
        except ClientError as e:
            print(f"Error applying policy: {e}")
