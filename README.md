# Riiid-Labs-Take-home-Assignment
Part of DevOps Engineering interview at Riiid Labs

## Tools/Technologies Used
1. Terraform - To provision the AWS Infrastructure 
2. AWS Lambda- A Python Lambda function to implement the business logic. Processing requests from the API Endpoint.
3. AWS API Gateway- To host HTTP API endpoint. Integrating it with the Lambda function. 
4. AWS S3- To the store the Terraform backend including the .tfstate files.

## Files
1. lambda.py- The Lambda function file with the handler function
2. lambda.py.zip- The zip file of the Lambda function to use as a Terraform resource
3. lambda.tf- The terraform file to provision the infrastructure

## Steps Followed
1. Configure AWS CLI locally
2. Create a new S3 bucket to use it as the Terraform backend
3. Provsion the infrastructure using Terraform by running the following commands
```
terraform init
terraform apply
```
4. Go the AWS console. Under API Gateway, you can the newly created HTTP API endpoint. 
5. Inside the AWS console, under Lambda, you can see the newly create python Lambda function. 

