import json
import boto3
import os
import uuid
from datetime import datetime
import base64

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])


def lambda_handler(event, context):
    for record in event['Records']:
        # Decode base64 payload
        decoded_data = base64.b64decode(
            record['kinesis']['data']).decode('utf-8')
        payload = json.loads(decoded_data)

        # Enrich and store
        payload['eventId'] = str(uuid.uuid4())
        payload['timestamp'] = datetime.utcnow().isoformat()

        table.put_item(Item=payload)

    return {
        'statusCode': 200,
        'body': json.dumps('Processed events')
    }
