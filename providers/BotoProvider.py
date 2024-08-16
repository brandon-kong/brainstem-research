from exceptions.SingletonException import (
    SingletonAlreadyLoadedException
)

import boto3

s3 = boto3.resource('s3')

class BotoProvider:
    """
    BotoProvider class
    An singleton abstract class to access AWS services such as S3 buckets for data storage.
    """

    __instance = None
    __boto_provider = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(BotoProvider, cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        pass
