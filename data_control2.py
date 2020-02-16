from pymongo import MongoClient
import json
import pymongo
from pymongo import MongoClient
from pprint import pprint
import random

client = MongoClient("mongodb+srv://Wen:1234@cluster0-gvhmp.mongodb.net/test?retryWrites=true&w=majority")
collectionUsers = client.interview.users
collectionData = client.interview.storedData

def get_av_emot():
    goodCount = 0
    badCount = 0
    for obj in client.interview.data.find():
        print("I am an emotion")
        if (obj['emot'] == 'good'):
            goodCount = goodCount +1
        else:
            badCount = badCount + 1
    if (goodCount + badCount == 0):
        return 0
    else:
        return (goodCount/(goodCount+badCount))

def get_img_data():
    pose_roll = 0
    pose_yaw = 0
    pose_pitch = 0
    n = 0
    smile = 0
    for obj in client.interview.users.find():
        print("I am an object")
        n += 1
        smileType = obj['FaceDetails'][0]['Smile']
        if smileType['Value']:
            smile += smileType['Confidence']
        else:
            smile -= smileType['Confidence']
        pose = obj['FaceDetails'][0]['Pose']

        pose_roll = max(abs(pose['Roll']), pose_roll)
        pose_pitch = max(pose_pitch, abs(pose['Pitch']))
        pose_yaw = max(abs(pose['Yaw']), pose_yaw)

        emot = obj['FaceDetails'][0]['Emotions']
        maxConf= -1
        maxEmot = "CALM"
        for emotion in emot:
            if float(emotion['Confidence']) > maxConf:
                maxEmot = emotion


        if (maxEmot == 'HAPPY' or maxEmot == 'CALM'):
            val = {'emot':'good'}
            val['_id'] = str(random.randint(1,23424))
            collectionData.insert_one(val)
        else:
            val = {'emot': 'good'}
            val['_id'] = str(random.randint(1, 23424))
            collectionData.insert_one(val)



#added over n_count for smile
    mydict = {'smile': (smile/n),
              'pose_roll': pose_roll,
              'pose_pitch': pose_pitch,
              'pose_yaw': pose_yaw,
              'good_emotion': get_av_emot()}

    return mydict