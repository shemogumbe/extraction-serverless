from google.cloud import vision
import json
import uuid

import boto3
import re

dynamodb = boto3.resource('dynamodb')
car_table = dynamodb.Table('front')
container_table = dynamodb.Table('rear')


def extract(file, front_or_rear):
    image_data = file.read()

    extraction = {}

    google_ocr_response = get_google_ocr_response(image_data)

    extraction['data'] = extract_data(google_ocr_response, front_or_rear)

    return extraction


def get_google_ocr_response(image_data):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    image = vision.types.Image(content=image_data)

    response = client.text_detection(image=image)

    return response


def extract_data(google_ocr_response, front_or_rear):
    text = str(google_ocr_response.full_text_annotation.text)
    if front_or_rear == 'front':
        req_text = re.findall(r"\s+(\w{3})[-.\s](\w{4})\s+", text)
    else:
        req_text = re.findall(r"(\w{3})(\w)\s*(\d{6})\s*(\d?)", text)
    if len(req_text):
        return req_text
    return [('None',)]


def home(event, context):
    creator = "Shem"
    body = f"{creator}'s app for extraction of truck info!"

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def front(event, context):

    if not event['image']:
        resp = {
            'statusCode': 400,
            'body': {'error': 'Invalid data'}
        }
        return resp
    extraction = extract(event['image'])
    car_table.put_item(
        Item={
            'registration_number': extraction
        }
    )
    resp = {
        'statusCode': 200,
        'body': "success"
    }

    return resp


def rear(event, context):
    if not event['image']:
        resp = {
            'statusCode': 400,
            'body': {'error': 'Invalid data'}
        }
        return resp
    extraction = extract(event['image'])
    container_table.put_item(
        Item={
            'registration_number': extraction
        }
    )
    resp = {
        'statusCode': 200,
        'body': extraction
    }

    return resp
