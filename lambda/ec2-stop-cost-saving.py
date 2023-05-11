import boto3
import os

client = boto3.client('ec2')

def lambda_handler(event, context):
    #Obtain all instances with "save_money" Tag in all region
    instances = []
    for region in client.describe_regions()['Regions']:
        ec2 = boto3.resource('ec2', region_name=region['RegionName'])
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        for instance in instances:
          print("Instance id - ", instance.id)
          print("Instance public IP - ", instance.public_ip_address)
          print("Instance private IP ", instance.private_ip_address)
          print("Region of Machine ", region)
          print("---------------------------------------------------------------------------------------")
          instance.stop()
