import boto3
from botocore.exceptions import ClientError

class CloudWatchManager:
    def __init__(self):
        self.cloudwatch = boto3.client('cloudwatch')

    def monitor_bucket(self, bucket_name):
        try:
            # Set up monitoring for the S3 bucket (e.g., storage usage)
            metric = self.cloudwatch.get_metric_data(
                MetricDataQueries=[
                    {
                        'Id': 's3Storage',
                        'MetricStat': {
                            'Metric': {
                                'Namespace': 'AWS/S3',
                                'MetricName': 'BucketSizeBytes',
                                'Dimensions': [
                                    {
                                        'Name': 'BucketName',
                                        'Value': bucket_name
                                    },
                                    {
                                        'Name': 'StorageType',
                                        'Value': 'StandardStorage'
                                    }
                                ]
                            },
                            'Period': 86400,
                            'Stat': 'Average'
                        }
                    }
                ],
                StartTime='2024-01-01T00:00:00Z',
                EndTime='2024-12-31T23:59:59Z'
            )
            print(f"Monitoring bucket {bucket_name} for storage usage.")
            print(metric)
        except ClientError as e:
            print(f"Error monitoring bucket: {e}")
