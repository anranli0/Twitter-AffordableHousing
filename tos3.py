import boto3
import os

def create_upload():
    s3 = boto3.client('s3')

    bucket_name = 'lsc-projct'
    bucket = s3.create_bucket(Bucket=bucket_name)

    dir = 'data'
    for filename in os.listdir(dir):
        if filename.endswith('.csv'): 
            key = filename
            path = os.path.join(dir, filename)
            print(path)
            s3.upload_file(Filename=path, Bucket=bucket_name, Key=key)


if __name__ == "__main__":
    create_upload()