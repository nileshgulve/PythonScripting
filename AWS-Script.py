
# BOTO3 - Is the AWS Software Development toolkit, using this manage all aws services by python code.

import boto3
# Launch AWS ec2 Instance
'''
 >Install boto3 module
 >pip install boto3
 >pip install awscli
 >aws configure
'''

ec2= boto3.resource('ec2')
# Create Instance
'''
isinstance= ec2.create_instances(
    ImageId= 'ami-045e6fa7127ab1ac4',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
print(isinstance[0].id)
'''
# Delete Instance

instance_id='i-0396b07b563b7447c'
instance=ec2.Instance(instance_id)
response= instance.terminate()
print(response)
