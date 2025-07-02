import json
import boto3
import os
import uuid
import logging
from datetime import datetime
import base64
from botocore.exceptions import ClientError

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DYNAMODB_TABLE')
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")

    for record in event['Records']:
        try:
            decoded_data = base64.b64decode(
                record['kinesis']['data']).decode('utf-8')
            payload = json.loads(decoded_data)

            # Add metadata
            payload['eventId'] = str(uuid.uuid4())
            payload['timestamp'] = datetime.utcnow().isoformat()

            table.put_item(Item=payload)
            logger.info(f"Successfully processed event: {payload['eventId']}")

        except (json.JSONDecodeError, KeyError) as parse_error:
            logger.error(f"Error parsing event data: {parse_error}")
        except ClientError as db_error:
            logger.error(f"Error writing to DynamoDB: {db_error}")

    return {
        'statusCode': 200,
        'body': json.dumps('Event processed')
    }


s3 = boto3.client('s3')
raw_bucket = os.environ.get('RAW_DATA_BUCKET')

# Inside lambda_handler loop:
try:
    # Save raw payload
    s3.put_object(
        Bucket=raw_bucket,
        Key=f"raw-events/{uuid.uuid4()}.json",
        Body=decoded_data,
        ContentType='application/json'
    )
except ClientError as s3_error:
    logger.error(f"Failed to write raw event to S3: {s3_error}")
