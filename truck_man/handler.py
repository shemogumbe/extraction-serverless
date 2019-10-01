import json
import extract


def home(event, context):
    creator = "Shem"
    body = f"{creator}'s app for extraction of truck info!"

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def front(event, context):
    extraction = extract.extract(event.files['file'], 'front')
    print('front', extraction['data'])
    return extraction


def rear(event, context):
    extraction = extract.extract(event.files['file'], 'rear')
    print('rear', extraction['data'])
    return extraction
