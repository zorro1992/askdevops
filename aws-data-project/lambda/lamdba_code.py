import json
import requests
import boto3
import uuid
import time
import random

def lambda_handler(event, context):
    #Create a clinet for kinesis, This uses boto3 which is imported above
    client = boto3.client('kinesis', region_name='region')

    #Partition key for passing to Kinesis , this is required to keep a unique ID
    partition_key = str(uuid.uuid4())
    
    # How many user information we need at a time.
    number_of_results = 500
    r = requests.get('https://randomuser.me/api/?exc=login&results=' + str(number_of_results))
    data = r.json()["results"]
    
    for i in range(10):
        random_user_index = int(random.uniform(0, (number_of_results - 1)))
        random_user = data[random_user_index]
        random_user = json.dumps(data[random_user_index])
        print("Starting to process , loop {}".format(i))
        client.put_record(
                StreamName='<USER-Data-Stream>',
                Data=random_user,
                PartitionKey=partition_key)
        print("Put record action is complete")
        time.sleep(random.uniform(0, 1))
        print("Sleeping now for sometime")
