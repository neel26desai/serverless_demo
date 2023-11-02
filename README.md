In this Serverless application, we use the cat API, to generate a new cat image every day at 9 am UTC, and save the image in S3.
Tech Used:
1. AWS SAM (Serverless architecture module) + Cloudformation - used for defining the Infrastructure as Code and deploying the serverless application
2. AWS S3 -place where we can store the data
3. AWS Lambda - Our serverless function
4. AWS EventBridge - Used for scheduling/ triggering our lambda every day at 9

File Structure
1. template.yaml - this file contains our SAM code, where we defined all out resources that we would need for running our application
2. samconfig.toml - contains the deployment configurations for our Serverless application
3. scripts/lambda_handler.py - contains the code that our lambda function will run
4. Makefile and requiements.txt - contains the requirements for generating a lambda layer
5. invoke_lambda.py - contains the code for manually invoking the lambda function for testing purposes
6. Serverless Assignment - has the screenshots for resource deployment,creations and deletion
