import boto3

client = boto3.client('ec2')
resp = client.run_instances(ImageId='ami-00c39f71452c08778', MaxCount=1, MinCount=1, InstanceType='t2.micro')

for x in resp['Instances']:
    print ('Your instance ID is {}'.format(x['InstanceId']))