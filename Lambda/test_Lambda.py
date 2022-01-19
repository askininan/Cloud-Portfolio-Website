import pytest
import boto3
import os
from dotenv import load_dotenv
from moto import mock_dynamodb2
from app import lambda_handler
import unittest


load_dotenv()

REGION = 'eu-central-1'

os.environ['DATABASENAME'] = 'testing'

class TestLambdaDDB(unittest.TestCase):
    @mock_dynamodb2
    def test_lambda_handler(self):

    
    # Create DynamoDB boto3 object
        dynamodb_c = boto3.client('dynamodb', 'eu-central-1')
    
    # Set dynamodb table name variable from env
        ddbTableName = os.environ['databaseName']     
        
    # Create mock DynamoDB table
        dynamodb_c.create_table(
            TableName = ddbTableName,
            BillingMode = 'PAY_PER_REQUEST',
            AttributeDefinitions = [{'AttributeName': 'id', 'AttributeType': 'S'}],
            KeySchema = [{'AttributeName': 'id', 'KeyType': 'HASH'}],
        )

        # Print Lambda response
        LambdaResponse = lambda_handler(0, 0)
        print('Lambda response: ', LambdaResponse)

        # Run unit test against Lambda status code
        self.assertStatus(200, LambdaResponse)