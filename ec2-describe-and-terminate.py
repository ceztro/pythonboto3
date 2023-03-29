import boto3

ec2 = boto3.resource('ec2')

for x in ec2.instances.all():
    print('your instance id is: {} and kernel id is {}. VPC ID is {}.'.format(x.instance_id,x.kernel_id,x.vpc_id))
    print('it has been created on {}'.format(x.launch_time))

devices = []

for x in ec2.instances.all():
    devices.append(x.instance_id)

decision = input('Do you want to remove all of the instances from that region? yes/no ')

if decision == 'yes':
    print('These instances will be removed: {}'.format(devices))
    for x in devices:
        ec2.Instance(x).terminate()