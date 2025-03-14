import json
import time

def lambda_handler_short(event, context):
    print("Hello World!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from short Lambda!')
    }

def lambda_handler_long(event, context):
    print("Going to sleep for 45 seconds")
    time.sleep(45)
    print("Woke up again!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from long Lambda!')
    }