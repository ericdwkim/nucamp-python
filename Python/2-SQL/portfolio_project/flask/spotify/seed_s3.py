"""
TODO: Populate AWS s3 bucket with personal audio files using AWS SDK.
"""


import os
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

"""
Load enviromental variables
"""
load_dotenv()
access_key = os.getenv('access_key')
access_secret = os.getenv('access_secret')
bucket_name = os.getenv('bucket_name')


def main():
    """
    Connect to S3 Service
    """
    client_s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret
    )

    print(client_s3)

    """
    Upload Files to S3 Bucket

    """
    data_file_path = os.path.join(os.getcwd(), 'audio_tracks')
    for file in os.listdir(data_file_path):
        if not file.startswith('~'):
            try:
                print('Uploading file {0}...'.format(file))
                client_s3.upload_file(
                    os.path.join(data_file_path, file),
                    bucket_name,
                    file
                )
            except ClientError as e:
                print('Credential is incorrect')
                print(e)
            except Exception as e:
                print(e)

    """
    Download Files to S3 Bucket

    """


if __name__ == '__main__':
    main()
