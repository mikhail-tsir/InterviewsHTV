# need to get authentication and setup instance

import boto3
import pymongo
from pymongo import MongoClient
from pprint import pprint
import json

cluster = MongoClient("mongodb+srv://Wen:1234@cluster0-gvhmp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["interview"]
collection = db["users"]

#can't be locally defined - need to hard code in conditions
#session = boto3.Session(profile_name='dev')

session = boto3.Session(aws_access_key_id='AKIAJVYGK2OK5VGO6CTA',
                        aws_secret_access_key='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',
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
    try:
        print([name, response['FaceDetails'][0]['Smile'], response['FaceDetails'][0]['Emotions']])
        try:
            collection.insert_one(response['FaceDetails'][0]['Smile'])
            collection.insert_one(response['FaceDetails'][0]['Emotions'])
        except:
            print("error uploading")

    #make it send to database instead of return
    except:
        print("error")


def analyzeAllPhotos(bucket):
    conn = session.client('s3')
    try:
        for key in conn.list_objects(Bucket=bucket)['Contents']:
            analyzePhoto(bucket, key['Key'])
    except:
        print("empty")
    try:
        for key in conn.list_objects(Bucket=bucket)['Contents']:
           # deleteFile(bucket, key['Key'])
            print("Helooo")
    except:
        print("empty")