# aws_sam_api_gateway
AWS SAM template examples for creating API Gateway calling Lambda functions synchronously / asynchronously

Calling a Lambda asynchronously from an API Gateway is especially required if the Lambda function runs longer than the maximum timeout of the API Gateway (currently 29 sec) to avoid that the API gateway returns a timeout error.

# Precondition
- Install and configure the SAM CLI
- Create an S3 bucket that can store the created stacks

# Creating a stack with a synchronous lambda call

```
sam deploy --template-file synchronous_lambda_call.yaml --capabilities CAPABILITY_IAM --stack-name synchronous-stack --s3-bucket YOUR_S3_BUCKET_NAME
```

The output at the end tells you which URL you can start in a browers, Postman, Insomnia, etc. to start the Lambda synchronously

# Creating a stack with an asynchronous lambda call

```
sam deploy --template-file asynchronous_lambda_call.yaml --capabilities CAPABILITY_IAM --stack-name asynchronous-stack --s3-bucket YOUR_S3_BUCKET_NAME
```

The output at the end tells you which URL you can start in a browers, Postman, Insomnia, etc. to start the Lambda asynchronously.

You can then watch the execution of the lambda function in the CloudWatch Logs stream that you find in the log group that corresponds to the Lambda.

# Delete stacks when not used anymore

```
aws cloudformation delete-stack --stack-name synchronous-stack
aws cloudformation delete-stack --stack-name asynchronous-stack
```