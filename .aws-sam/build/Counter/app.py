import json
import boto3
import os

# Initialize dynamodb boto3 object
dynamodb = boto3.resource('dynamodb')
# Set dynamodb table name variable from env
ddbTableName = os.environ['databaseName']
table = dynamodb.Table(ddbTableName)

def lambda_handler(event, context):
    # Update item in table or add if doesn't exist
    ddbResponse = table.update_item(
        Key={
            'id': 'VisitorCount'
        },
        UpdateExpression='ADD ' + 'VisitorCount' + ' :increment',
        ExpressionAttributeValues={
            ':increment': 1
        },
        ReturnValues="UPDATED_NEW"
    )

    # Format dynamodb response into variable
    responseBody = json.dumps({"Visitor Count": int(float(ddbResponse["Attributes"]["VisitorCount"]))})

    # Create api response object
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": responseBody,
        "headers": {
        "Access-Control-Allow-Headers" : "*",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "*",
        "Access-Control-Allow-Methods": "GET,OPTIONS",
        "Content-Type": "application/json" 
        }
    }

    # Return api response object
    return apiResponse