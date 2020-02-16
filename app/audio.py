import boto3
import json
import time

session = boto3.Session(aws_access_key_id='AKIAJKXVIYSIIRZYA2UQ',
                        aws_secret_access_key='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',
                        region_name='us-east-1')

client = session.client('s3')

#bucket != target is best
def transcribeAudio(bucket, name, target):
    object_url = f"https://{bucket}.s3.amazonaws.com/{name.replace(' ', '+')}"
    client_transcribe = session.client('transcribe')
    client_transcribe.start_transcription_job(
        TranscriptionJobName=name,
        Media={'MediaFileUri': object_url},
        MediaFormat='wav',
        LanguageCode='en-US',
        OutputBucketName=target)
    while True:
        status = client_transcribe.get_transcription_job(TranscriptionJobName=name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            print("Finished Transcription.")
            break
        print("Loading...")
        time.sleep(5)
