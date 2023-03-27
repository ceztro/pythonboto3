import boto3
from ec2_metadata import ec2_metadata

print(ec2_metadata.instance_id)

