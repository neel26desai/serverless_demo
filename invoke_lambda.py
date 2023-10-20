import boto3
import requests
from datetime import datetime
import json
# create a boto3 client for lambda
client = boto3.client('lambda')

# define the name of the lambda function to invoke
function_name = 'MyLambdaFunction'

# define the payload to pass to the lambda function
payload = {
    'key1': 'value1',
    'key2': 'value2'
}

# invoke the lambda function with the payload
response = client.invoke(
    FunctionName=function_name,
    Payload=json.dumps(payload)
)

# print the response from the lambda function
print(response['Payload'].read().decode())







