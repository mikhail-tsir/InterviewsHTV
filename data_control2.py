from pymongo import MongoClient
import json
import pymongo
from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://Wen:1234@cluster0-gvhmp.mongodb.net/test?retryWrites=true&w=majority")
collectionUsers = client.interview.users
collectionData = client.interview.storedData

def get_av_emot():
    goodCount = 0
    badCount = 0
    for obj in collectionData.interview.data.find():
        if (obj == 'good'):
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
    for obj in collectionUsers.interview.users.find():
        n += 1
        smile = obj['FaceDetails'][0]['Smile']
        pose = obj['FaceDetails']['Pose']

        pose_roll = max(abs(pose['Roll']), pose_roll)
        pose_pitch = max(pose_pitch, abs(pose['Pitch']))
        pose_yaw = max(abs(pose['Yaw']), pose_yaw)

        emot = obj['FaceDetails'][0]['Emotions']
        if emot[0]['Type'] == 'HAPPY' or emot[0]['Type'] == 'CALM':
            collectionData.insert_one(json.dumps('good'))
        else:
            collectionData.insert_one(json.dumps('bad'))



#added over n_count for smile
    mydict = {'smile': smile,
              'pose_roll': pose_roll,
              'pose_pitch': pose_pitch,
              'pose_yaw': pose_yaw,
              'good_emotion': get_av_emot()}

    return mydict