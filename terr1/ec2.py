import boto3

ec2 = boto3.resource('ec2',region_name='us-east-1')
instances = ec2.instances.filter(
  Filters=[{'Name':'instance-state-name', 'Values':['stopped']}]
)

for instance in instances:
  print(f"ID: {instance.id}, State: {instance.state['Name']}")
