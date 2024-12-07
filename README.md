# AWS S3 Bucket Manager

A Python-based tool to manage AWS S3 buckets, including functionalities for creating, deleting, uploading files, applying IAM policies, and monitoring bucket usage with AWS CloudWatch.

## Features

- **Create S3 Bucket**: Automatically create an S3 bucket on AWS.
- **Delete S3 Bucket**: Delete an existing S3 bucket.
- **Upload Files to S3**: Upload local files to a specified S3 bucket.
- **Apply IAM Policy**: Attach a custom IAM policy to an S3 bucket for security.
- **Monitor S3 Bucket**: Use AWS CloudWatch to monitor storage usage of an S3 bucket.

## Requirements

- Python 3.x
- [boto3](https://boto3.amazonaws.com/) (AWS SDK for Python)
- AWS CLI configured with valid credentials (`aws configure`)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/pantelovich/aws-s3-bucket-manager.git
   cd aws-s3-bucket-manager
2. Install the dependencies:

   ```bash
   pip install boto3
3. Configure AWS CLI with your credentials:

   ```bash
   aws configure
   Usage
   Create a New Bucket
4. To create a new S3 bucket:

   ```bash
   python main.py --create bucket_name
   Delete an Existing Bucket
5. To delete an S3 bucket:

   ```bash
   python main.py --delete bucket_name
   Upload a File to a Bucket
6. To upload a file to a specified S3 bucket:

   ```bash
   python main.py --upload --bucket bucket_name --file file_name
   Apply an IAM Policy to a Bucket
7. To apply an IAM policy to a specified S3 bucket:

   ```bash
   python main.py --policy policy_name --bucket bucket_name
   Monitor S3 Bucket Usage with CloudWatch
8. To monitor the usage of a bucket via CloudWatch:

   ```bash
   python main.py --monitor bucket_name
   License
This project is licensed under the MIT License.

markdown
Copy code

### Key improvements:
- Proper markdown formatting with code blocks.
- Clear structure for GitHub compatibility.
- Links for dependencies like `boto3` are correctly formatted.
- Section headers and usage instructions are well-structured for clarity.
