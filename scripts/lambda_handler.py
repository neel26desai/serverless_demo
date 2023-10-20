import boto3
import requests
from datetime import datetime


s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'neel-sjsu'
    now = datetime.now()
    suffix = now.strftime('%y%m%d%H%M')
    file_name= f"cats/random_cat_{suffix}.jpg"
    # Get the image content
    image_url = requests.get("https://api.thecatapi.com/v1/images/search").json()[0]['url']
    image_content = requests.get(image_url).content

    # Upload the image to S3
    s3_client.put_object(Body=image_content, Bucket=bucket_name, Key=file_name)
    #return the path to the image as requested by the API
    return f'https://s3.amazonaws.com/{bucket_name}/{file_name}'

