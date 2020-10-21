# Riiid-Labs-Take-home-Assignment
Part of DevOps Engineering interview at Riiid Labs

## Tools/Technologies Used
1. Terraform - To provision the AWS Infrastructure 
2. AWS Lambda- A Python Lambda function to implement the business logic. Processing requests from the API Endpoint.
3. AWS API Gateway- To host HTTP API endpoint. Integrating it with the Lambda function. 
4. AWS S3- To the store the Terraform backend including the .tfstate files.

## Steps Followed
1. Configure AWS CLI locally
2. Create a new S3 bucket to use it as the Terraform backend
2. Provsion the infrastructure using Terraform by running the following commands
```
terraform init
terraform apply
```

