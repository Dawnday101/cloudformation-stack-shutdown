import boto3
import re  
import datetime
import logging
ec2 = boto3.resource('ec2')
ec = boto3.client('ec2', region_name='us-east-1')  
iam = boto3.client('iam')
def lambda_handler(event, context):
    client = boto3.client('cloudformation')
    response = client.delete_stack(StackName='your-stack-name')
    return(response)
