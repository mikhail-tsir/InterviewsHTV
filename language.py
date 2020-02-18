import boto3
import json


session = boto3.Session(aws_access_key_id='AWS_ACCESS_KEY',
                        aws_secret_access_key='AWS_SECRET_KEY',
                        region_name='us-east-1')

comprehend = session.client('comprehend')

textBucket = 'hack-the-valley-text'

s3 = boto3.resource('s3')

def getTranscript(bucket):
    jsonText = getFirstFile(textBucket)
    try:
        return jsonText['results']['transcripts'][0]['transcript']
    except:
        return "error"

def detectKeyPhrases(input):
    return comprehend.detect_key_phrases(Text=input, LanguageCode='en')

def detectSentiment(input):
    return comprehend.detect_sentiment(Text=input, LanguageCode='en')

def calculateSpeed(input):
    time = 90
    words = len(input.split())
    return words*60/time

'''def processLanguage(name):
    content_object = s3.Object('hack-the-valley-text', name)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    input = str(json_content['results']['transcripts'][0]['transcript'])
    print(input)
    keyPhraseJson = detectKeyPhrases(input)
    sentimentJson = detectSentiment(input)
    sentiment = sentimentJson['Sentiment']
    sentimentPercent = sentimentJson['SentimentScore'][sentiment.lower().capitalize()]
    phrases = keyPhraseJson['KeyPhrases']
    phraseList = [];
    for dictionary in phrases:
        phraseList.append(dictionary['Text'])
    output = [sentiment, sentimentPercent, phraseList, calculateSpeed(input)]
    print(output)
    return output'''

def processLanguage(name):
    content_object = s3.Object('hack-the-valley-text', name)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    input = str(json_content['results']['transcripts'][0]['transcript'])
    print(input)
    keyPhraseJson = detectKeyPhrases(input)
    sentimentJson = detectSentiment(input)
    sentiment = sentimentJson['Sentiment']
    sentimentPercent = sentimentJson['SentimentScore'][sentiment.lower().capitalize()]
    phrases = keyPhraseJson['KeyPhrases']
    phraseList = [];
    for dictionary in phrases:
        phraseList.append(dictionary['Text'])
    output = [sentiment, sentimentPercent, phraseList, calculateSpeed(input)]
    print(output)
    return output
    #except:
     #   print("error in processing language")
      #  return ["", -1, [], -1]


