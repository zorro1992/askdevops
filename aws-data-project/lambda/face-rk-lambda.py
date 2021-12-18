import json
import boto3

def lambda_handler(event, context):
  
    BUCKET = "face-rk-2021"
    KEY = "bollywood_1.png"
    
    def detect_faces(bucket, key, region="eu-central-1"):
        rekognition = boto3.client("rekognition", region)
        response = rekognition.recognize_celebrities(Image={'S3Object':{'Bucket': bucket,'Name': key}})
        for celebrity in response['CelebrityFaces']:
    	    print ('Name: ' + celebrity['Name'])
    
    detect_faces(BUCKET,KEY)
