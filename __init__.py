from flask import Flask
from flask_cors import CORS
from .sendImage import getImage
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
from data_control import ImageData
from getAudio import sendAudio
from give_tips import givetips
from stallWords import getStall
from __main__ import requestPhotos
from language import processLanguage
from generate_question import gen_q
import json

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
    return json.dump([])


@app.route('/photo')
def takePhoto():
    getImage(10)
    return json.dump([])


@app.route('/pdata')
def photoData():
    analyzeAllPhotos(photoBucket)
    data = ImageData.get_img_data()
    return json.dump(givetips(data))

@app.route('/ldata')
def languageData():
    transcribeAudio(audioBucket, textBucket)
    return json.dump(processLanguage())

@app.route('/question')
def sendQuestion():
    return json.dumps(gen_q())



@app.route('/')
def home():
    return 'owo'