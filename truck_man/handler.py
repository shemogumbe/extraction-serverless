import json
import uuid

import boto3


def home(event, context):
    creator = "Shem"
    body = f"{creator}'s app for extraction of truck info!"

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def front(event, context):
    body = json.loads(event['body'])
    resp = {
        'statusCode': 200,
        'body': "success"
    }
    # extraction = extract.extract(event.files['file'], 'front')
    # print('front', extraction['data'])
    return resp


def rear(event, context):
    resp = {
        'statusCode': 200,
        'body': "success"
    }
    # extraction = extract.extract(event.files['file'], 'front')
    # print('front', extraction['data'])
    return resp
