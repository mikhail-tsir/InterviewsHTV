from stallWords import getStall


import boto3
from botocore.client import Config
import os
import random
import pymongo
from pymongo import MongoClient
from pprint import pprint
cluster = MongoClient("mongodb+srv://Wen:1234@cluster0-gvhmp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["interview"]
collection = db["users"]

#here = os.path.dirname(os.path.abspath(__file__))

#filename = os.path.join(here, 'example.jpg')
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIAJVYGK2OK5VGO6CTA'
SECRET_KEY = 'mksqTMZbV5BHJhJUU7HmU8eVA356a4/kXIXIOQ1H'
bucketname = 'new-hack-valley'
#data = open(filename, 'rb')

s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                    config = Config(signature_version='s3v4'))

import cv2, time
video = cv2.VideoCapture(0)
a = 0
while True:
    a = a + 1
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'example.jpg')
    data = open(filename, 'rb')
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gener = random.randint(1, 10000)
    if a % 10 == 0:
        cv2.imwrite(filename, frame)
        s3.Bucket(bucketname).put_object(Key="{}.jpg".format(gener), Body=data)

print (getStall("hi im um like a person"))