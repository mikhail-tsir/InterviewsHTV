from photo import analyzePhoto, deleteFile, getFiles, analyzeAllPhotos
from audio import transcribeAudio
from language import processLanguage
import boto3
from stallWords import getStall
from sendImage import getImage
from getAudio import sendAudio
import threading
import time
from getAudio import sendAudio
from give_tips import givetips
from stallWords import getStall
from generate_question import gen_q
from photo import clearFiles
from __init__ import photoData
from __init__ import takePhoto
from __init__ import recAud
from __init__ import sendQuestion
from __init__ import stop
from __init__ import languageData
from audio import getFirstFile
from language import processLanguage
from data_control2 import get_img_data


#make class having folder name ? triv
#deleteFile('new-hack-valley', 'bad_example.jpg')

photoBucket = 'hack-the-valley-photo'
audioBucket = 'hack-the-valley-audio'
textBucket = 'hack-the-valley-text'

session = boto3.Session(aws_access_key_id='AKIAIWMAC56IM4LRHWUA',
                        aws_secret_access_key='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',
                        region_name='us-east-1')

#t1 = threading.Thread(target=getImage, args=(100,))
#t2 = threading.Thread(target=sendAudio, args=(20,))
#t3 = threading.Thread(target=updateDataLoop, args=())


def sendTips(data):
    tips = givetips(data)
    #send tips to react


def requestAudio():
    sendAudio(90)


def requestPhotos():
    getImage(10)

def requestData():
    analyzeAllPhotos(photoBucket)
    data = get_img_data()
    return data
    #send get_tips([data[0], data[1], data[2], ...]) to react

def start():
    requestAudio()
    requestPhotos()


def __main__():
    print("Hello, World!")






#analyzeAllPhotos(photoBucket)
#transcribeAudio(audioBucket, '67228168465412459108694491266449718741810309510441950878908.wav', textBucket)

#clearBucket(audioBucket)

#processLanguage("I constantly display a good work ethic, if someone asks me to do something, I'll do it no matter what.")
#transcribeAudio(audioBucket, '67683272999951193819036946770628923121386908970706710153232.wav', textBucket)


stop()
takePhoto()
print(photoData())


'''
stop()
recAud()
print(languageData())
'''