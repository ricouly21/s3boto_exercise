import uuid
import boto3
import configparser
from datetime import datetime as dt

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

config = configparser.ConfigParser()
config.read(".aws/config")
config = config['default']


class S3Helper(object):

    @staticmethod
    def upload_file(orig_filename, folder, filename_hash):
        try:
            s3_client = boto3.client(
                "s3",
                aws_access_key_id=config['aws_access_key_id'],
                aws_secret_access_key=config['aws_secret_access_key'],
            )
            object_name = '{}/{}'.format(folder, filename_hash)
            s3_client.upload_file(orig_filename, config['aws_s3_bucket'], object_name)
            return {
                "status": HTTP_200_OK,
                "upload_url": "http://{0}/{1}".format(config['aws_s3_bucket_url'], object_name),
                "message": "Upload successful!",
            }
        except TypeError as error:
            return {"status": HTTP_400_BAD_REQUEST, "message": error}
