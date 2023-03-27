import boto3
from ec2_metadata import ec2_metadata

ec2 = boto3.resource('ec2')
ids = []

while True:
    x= input('Please provide an instance you would like to terminate: ')
    ids.append(str(x))
    answer=input('would you like to add another one? yes/no - ')
    if answer == 'yes':
        continue
    else:
        break


print('following instances will be terminated: {}'.format(ids))
security_check = input('To terminate please type "I want to terminate" - ')
if security_check == 'I want to terminate':
    ec2.instances.filter(InstanceIds=ids).terminate()
else:
    print("No machines were terminated")



