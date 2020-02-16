from flask import Flask
from flask_cors import CORS
import os
import random
from photo import analyzePhoto, deleteFile, getFiles, analyzeAllPhotos
from audio import transcribeAudio
from language import processLanguage
import boto3
from stallWords import getStall
from sendImage import getImage
from getAudio import sendAudio
import threading
import time
from data_control2 import get_img_data
from getAudio import sendAudio
from give_tips import givetips
from stallWords import getStall
from __main__ import requestPhotos
from language import processLanguage
from generate_question import gen_q
import json
from photo import clearFiles

app = Flask(__name__)
CORS(app)

photoBucket = 'hack-the-valley-photo'
audioBucket = 'hack-the-valley-audio'
textBucket = 'hack-the-valley-text'


'''
4 http process:
1 - start sound
2 - take a photo
3 - process photos and return data
4 - process audio and return data
5 - return a question'''

@app.route('/audio')
def recAud():
    sendAudio(90)
    return json.dumps([])


@app.route('/photo')
def takePhoto():
    getImage(10)
    return json.dumps([])


@app.route('/pdata')
def photoData():
    analyzeAllPhotos(photoBucket)
    data = get_img_data()
    print(json.dumps(givetips(data)))
    return json.dumps(givetips(data))

@app.route('/ldata')
def languageData():
    transcribeAudio(audioBucket, textBucket)
    return json.dumps(processLanguage())

@app.route('/question')
def sendQuestion():
    return json.dumps(gen_q())

@app.route('/stop')
def stop():
    clearBucket('hack-the-valley-photo')
    clearBucket('hack-the-valley-audio')
    clearBucket('hack-the-valley-text')


@app.route('/')
def home():
    return 'owo'

takePhoto()