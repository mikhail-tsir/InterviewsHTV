import boto3
import json


session = boto3.Session(aws_access_key_id='AKIAJVYGK2OK5VGO6CTA',
                        aws_secret_access_key='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',
                        region_name='us-east-1')

comprehend = session.client('comprehend')

def detectKeyPhrases(input):
    return comprehend.detect_key_phrases(Text=input, LanguageCode='en')

def detectSentiment(input):
    return comprehend.detect_sentiment(Text=input, LanguageCode='en')

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
        output = [sentiment, sentimentPercent, phraseList]
        print(output)
        return output
    except:
        print("error in processing language")
        return ["", -1, []]


