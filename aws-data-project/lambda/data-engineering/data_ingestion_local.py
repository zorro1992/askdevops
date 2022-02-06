import json
import requests
import boto3
import uuid
import time
import random

def lambda_handler(event, context):

    number_of_results = 500
    r = requests.get('https://randomuser.me/api/?exc=login&results=' + str(number_of_results))
    data = r.json()["results"]
    print(data)
    print(type(data))
