from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://Wen:1234@cluster0-gvhmp.mongodb.net/test?retryWrites=true&w=majority")
collection = client.interview.users

def get_img_data():

    smile_count = 0
    eye_count = 0
    happy = 0
    calm = 0
    angry = 0
    disgust = 0
    fear = 0
    surprise = 0
    sad = 0
    confused = 0
    count = 0

    for obj in collection.find():
        smile = obj['FaceDetails'][0]['Smile']
        if smile['Value']:
            smile_count += smile['Confidence']

        eyes = obj['FaceDetails'][0]['EyesOpen']
        if eyes['Value']:
            eye_count += eyes['Confidence']

        for emot in obj['FaceDetails'][0]['Emotions']:
            if emot['Type'] == 'HAPPY':
                happy += emot['Confidence']
            elif emot['Type'] == 'CALM':
                calm += emot['Confidence']
            elif emot['Type'] == 'ANGRY':
                angry += emot['Confidence']
            elif emot['Type'] == 'DISGUSTED':
                disgust += emot['Confidence']
            elif emot['Type'] == 'FEAR':
                fear += emot['Confidence']
            elif emot['Type'] == 'SURPRISED':
                surprise += emot['Confidence']
            elif emot['Type'] == 'SAD':
                sad += emot['Confidence']
            elif emot['Type'] == 'CONFUSED':
                confused += emot['Confidence']
            print(obj)

            count += 1
    mydict = {'smile': smile_count / count,
              'eye_contact': eye_count / count,
              'happy': happy / count,
              'sad': sad / count,
              'angry': angry / count,
              'confused': confused / count,
              'surprised': surprise / count,
              'calm': calm / count,
              'disgusted': disgust / count,
              'fear': fear / count}
    print(mydict)
    return json.dumps(mydict)
get_img_data()


