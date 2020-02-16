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
from generate_question import gen_q

#make class having folder name ? triv
#deleteFile('new-hack-valley', 'bad_example.jpg')

photoBucket = 'hack-the-valley-photo'
audioBucket = 'hack-the-valley-audio'
textBucket = 'hack-the-valley-text'

session = boto3.Session(aws_access_key_id='AKIAJKXVIYSIIRZYA2UQ',
                        aws_secret_access_key='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',
                        region_name='us-east-1')

#t1 = threading.Thread(target=getImage, args=(100,))
#t2 = threading.Thread(target=sendAudio, args=(20,))
#t3 = threading.Thread(target=updateDataLoop, args=())

def clearBucket(bucket):
    conn = session.client('s3')
    s3 = boto3.resource('s3')
    try:
        for key in conn.list_objects(Bucket=bucket)['Contents']:
            s3.Object(bucket, key['Key']).delete()
    except:
        print("empty bucket")


def sendTips(data):
    tips = givetips(data)
    #send tips to react


def requestAudio():
    sendAudio(90)


def requestPhotos():
    getImage(10)

def requestData():
    analyzeAllPhotos(photoBucket)
    data = ImageData.get_img_data()
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