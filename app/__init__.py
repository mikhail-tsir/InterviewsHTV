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

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def thing():
	requestPhotos()
	processLanguage()
	
	return "owo"
	
@app.route('/')
def home():
    return 'owo'

