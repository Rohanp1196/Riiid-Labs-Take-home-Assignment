# Riiid-Labs-Take-home-Assignment
Part of DevOps Engineering interview at Riiid Labs

## Tools/Technologies Used
1. Terraform - To provision the AWS Infrastructure 
2. AWS Lambda- A Python Lambda function to implement the business logic. Processing requests from the API Endpoint.
3. AWS API Gateway- To host HTTP API endpoint. Integrating it with the Lambda function. 
4. AWS S3- To the store the Terraform backend including the .tfstate files.
5- Circle CI-  A CI/CD tool to automate the build and deploy process

## Files
1. lambda.py- The Lambda function file with the handler function
2. lambda.py.zip- The zip file of the Lambda function to use as a Terraform resource
3. lambda.tf- The terraform file to provision the infrastructure
4. .circle/config.yml- The configuration file for the pipeline on Circle CI

## Workflow (Manual)
1. Configure AWS CLI locally
2. Create a new S3 bucket to use it as the Terraform backend
3. Provsion the infrastructure using Terraform by running the following commands
```
terraform init
terraform apply
```
The **tfstate** has been uploaded to the **S3 Bucket**

4. Go the AWS console. Under API Gateway, you can the newly created HTTP API endpoint. 
5. Inside the AWS console, under Lambda, you can see the newly create python Lambda function. 

## Workflow (Automated through Circle CI)
1. Create a Circle CI account.
2. Link it with your GitHub account to get all the repositories connected with your Circle CI account.
3. Create a *config.yml* under *.circleci* directory in your project repository with the pipeline execution jobs and tasks.
5. Add your **AWS_ACCESS_KEY_ID & AWS_SECRET_ACCESS_KEY** as environement variable under your project settings in Circle CI. This would allow access to AWS.
6. Any commit to the repository would trigger the CI pipleine on Circle CI.
7. It follows 4 steps as shown in the below figure:

![Pipeline](/images/pipeline.png)

### To Provision the infrastructure
Step A: Generating the terraform plan for the infrastructure.

*------Waiting for Approval-----*

Step B: Applying the terraform plan and storing the state in S3 Backend.

### To Destroy the infrastructure
Step C: Generating a Destroy plan.

*------Waiting for Approval-----*

Step D: Destroying the infrastructure.

## Business Logic

I was not being able to successfully implement the business logic required in the API. Although, I have done a different task:
```
 base_url = 'https://hacker-news.firebaseio.com/v0/item/'
    answer = []
    for itemid in range(1, 10):
    # Get item
        item_response = urllib.request.urlopen(base_url + str(itemid) + '.json')
        response_string = item_response.read().decode('utf-8')
        item = json.loads(response_string)
        time = item['time']
        ts = int(time)
        ans = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        answer.append(ans)
    return answer
```
Getting the dates of the first 10 articles on Hacker News. 




