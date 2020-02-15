import boto3

#can't be locally defined - need to hard code in conditions
#session = boto3.Session(profile_name='dev')

session = boto3.Session(aws_access_key_id='XXXXXXXXXXXX',
                        aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXX',
                        region_name='us-east-1')
s3 = boto3.resource('s3')


client = session.client('transcribe')

def getFiles(bucket):
    conn = session.client('s3')
    for key in conn.list_objects(Bucket=bucket)['Contents']:
        print(key['Key'])

def deleteFile(bucket, name):
    s3.Object(bucket, name).delete()

def analyzeAudio(bucket, name):
    response = client.start_transcription_job(
        #need different names for every single transcription job
        TranscriptionJobName = 'text_output2',
        LanguageCode = 'en-US',
        #MediaSampleRateHertz=123 ,
        MediaFormat = 'wav',
        Media = {
                    'MediaFileUri': 'https://hack-the-valley-audio.s3.amazonaws.com/sample_audio.wav'
                },
        OutputBucketName = 'hack-the-valley-text',
        #OutputEncryptionKMSKeyId = 'string',
        Settings = {
                      # 'VocabularyName': 'string',
                      # 'ShowSpeakerLabels': True | False,
                      # 'MaxSpeakerLabels': 123,
                      # 'ChannelIdentification': True | False,
                     #  'ShowAlternatives': True | False,
                     #  'MaxAlternatives': 123,
                       #'VocabularyFilterName': 'string',
                       #'VocabularyFilterMethod': 'remove' | 'mask'
                   },
        JobExecutionSettings = {
           # 'AllowDeferredExecution': True | False,
           # 'DataAccessRoleArn': 'string'
        }

    )
    print(response)

def analyzeAllAudio(bucket):
    conn = session.client('s3')
    for key in conn.list_objects(Bucket=bucket)['Contents']:
        analyzeAudio(bucket, key['Key'])

    for key in conn.list_objects(Bucket=bucket)['Contents']:
        deleteFile(bucket, key['Key'])
