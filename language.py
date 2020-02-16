import boto3
import json


session = boto3.Session(aws_access_key_id='AKIAJKXVIYSIIRZYA2UQ',
                        aws_secret_access_key='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',
                        region_name='us-east-1')

comprehend = session.client('comprehend')

def detectKeyPhrases(input):
    return comprehend.detect_key_phrases(Text=input, LanguageCode='en')

def detectSentiment(input):
    return comprehend.detect_sentiment(Text=input, LanguageCode='en')

def calculateSpeed(input):
    time = 90
    words = input.split().length()
    return words*60/time

def processLanguage(input):
    try:
        keyPhraseJson = detectKeyPhrases(input)
        sentimentJson = detectSentiment(input)
        sentiment = sentimentJson['Sentiment']
        sentimentPercent = sentimentJson['SentimentScore'][sentiment.lower().capitalize()]
        phrases = keyPhraseJson['KeyPhrases']
        phraseList = [];
        for dictionary in phrases:
            phraseList.append(dictionary['Text'])
        output = [sentiment, sentimentPercent, phraseList, calculateSpeed(input), ]
        print(output)
        return output
    except:
        print("error in processing language")
        return ["", -1, [], -1]


