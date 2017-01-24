import boto3 as aws # This is the aws resource library
import json

# Denote we are using s3
s3 = aws.resource('s3')

# Denote a bucket name and filename
obj = s3.Object(bucket_name='info370-lab-03', key="sample.json")

# Actually pull down that file (this gives us a response object)
res = obj.get()

# Get the body of the response (this will be raw bytes)
raw_data = res['Body'].read().decode('utf-8')

# Read the file as json
data = json.loads(raw_data)

# Data is a dictionary. Access they key mystery and print the value in the
# dictionary to the console. You should save your changes to this file
# on the server to receive participation for the day.
