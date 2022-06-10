import json
import boto3
from datetime import datetime

#Lambda 2 - Transform function

def transformation():
    s3 = boto3.resource('s3')
    bucket = "biproyecto"
    file = "tweets/CD.json"

    content_object = s3.Object(bucket, file)

    file_content = content_object.get()['Body'].read().decode('utf-8')

    json_content = json.loads(file_content)
    # x = json_content[1]

    list = []
    list.append(json_content[0])
    dateApi = json_content[0]
