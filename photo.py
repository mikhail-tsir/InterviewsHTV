# need to get authentication and setup instance

import boto3
import pymongo
from pymongo import MongoClient
from pprint import pprint
import json

cluster = MongoClient("mongodb+srv://Wen:[PASSWORD]@cluster0-gvhmp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["interview"]
collection = db["users"]

session = boto3.Session(aws_access_key_id='AWS_ACCESS_KEY',
                        aws_secret_access_key='AWS_PRIVATE_KEY',
                        region_name='us-east-1')
s3 = boto3.resource('s3')


client = session.client(
    'rekognition')

def getFiles(bucket):
    conn = session.client('s3')
    for key in conn.list_objects(Bucket=bucket)['Contents']:
        print(key['Key'])

def deleteFile(bucket, name):
    s3.Object(bucket, name).delete()

def clearFiles(bucket):
    try:
        conn = session.client('s3')
        for key in conn.list_objects(Bucket=bucket)['Contents']:
            deleteFile(bucket, key['Key'])
        print("Cleared.")
    except:
        print("Empty bucket")
def analyzePhoto(bucket, name):
    response = client.detect_faces(
        Image={
            #'Bytes': b'bytes',
            'S3Object': {
                'Bucket': bucket,
                'Name': name,
                #'Version': version
            }
        },
        #don't actually use all attributes - makes faster
        Attributes=[ 'ALL'

        ]
    )
    print([name, response['FaceDetails'][0]['Smile'], response['FaceDetails'][0]['Emotions']])
    entry = response
    entry['_id'] = name
    collection.insert_one(entry)


def analyzeAllPhotos(bucket):
    conn = session.client('s3')
    #add while true? while running?
    #try:
    for key in conn.list_objects(Bucket=bucket)['Contents']:
        analyzePhoto(bucket, key['Key'])
        deleteFile(bucket, key['Key'])
    #except:
     #   print("empty")
