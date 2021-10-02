#AWS SDK for python 
import boto3

#object 
client = boto3.client('s3')

#list_objects is an API
#Bucket = test bucket
response = client.list_objects(Bucket='aws-bma-test')

#iterate response
for content in response['Contents']:
    obj_dict = client.get_object(Bucket='aws-bma-test', Key=content['Key'])
    print(content['Key'], obj_dict['LastModified'])
    
