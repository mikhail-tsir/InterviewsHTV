
import sounddevice as sd
from scipy.io.wavfile import write
import os
import boto3
from botocore.client import Config
import os
import random
ACCESS_KEY = 'AKIAJVYGK2OK5VGO6CTA'
SECRET_KEY = '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'
bucketname = 'hack-the-valley-audio'
#data = open(filename, 'rb')

s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                    config = Config(signature_version='s3v4'))
def sendAudio(length):
    fs = 44100  # this is the frequency sampling; also: 4999, 64000
    seconds = length  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    print("Starting: Speak now!")
    sd.wait()  # Wait until recording is finished
    print("finished")
    here1 = os.path.dirname(os.path.abspath(__file__))
    filename1 = os.path.join(here1, 'myaudio.wav')
    data1 = open(filename1, 'rb')
    write(filename1, fs, myrecording)  # Save as WAV file
    # os.startfile("myaudio.wav")
    generaudio = random.randint(1, 100000000000000000000000000000000000000000000000000000000000)

    s3.Bucket(bucketname).put_object(Key="{}.wav".format(generaudio), Body=data1)
