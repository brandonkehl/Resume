
import json
import boto3
import datetime


def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    count = dynamodb.Table('Visits')
    
    
    
    # Putting a try/catch to log to user when some error occurs
    try:
        
        count.put_item(
           Item={
                'count': {'N': 'count'}
                
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfull')
        }
    except:
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving the data')
        }