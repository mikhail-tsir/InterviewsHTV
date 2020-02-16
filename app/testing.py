from pymongo import MongoClient
import json


class ImageData:
    client = MongoClient("mongodb+srv://Wen:1234@cluster0-gvhmp.mongodb.net/test?retryWrites=true&w=majority")
    collection = client.interview.users

    good_emotion_count = 0
    bad_emotion_count = 0
    smile_count = 0
    n_count = 0
    sunglasses = False  # only checks first frame for sunglasses, stores it in this variable
    _sunglass_check = False  # ignore this

    @staticmethod
    def get_img_data():
        global collection, smile_count, good_emotion_count, bad_emotion_count, sunglasses, _sunglass_check, n_count
        pose_roll = 0
        pose_yaw = 0
        pose_pitch = 0
        n = 0
        for obj in collection.find():
            n += 1
            if not ImageData._sunglass_check:
                if obj['FaceDetails'][0]['Sunglasses']['Value']:
                    sunglasses = True
                _sunglass_check = True
            smile = obj['FaceDetails'][0]['Smile']
            if smile['Value']:
                smile_count += smile['Confidence']
            else:
                smile_count -= smile['Confidence']

            pose = obj['FaceDetails']['Pose']

            pose_roll += pose['Roll']
            pose_pitch += pose['Pitch']
            pose_yaw += pose['Yaw']

            emot = obj['FaceDetails'][0]['Emotions']
            if emot[0]['Type'] == 'HAPPY' or emot[0]['Type'] == 'CALM':
                ImageData.good_emotion_count += emot[0]['Confidence']
            else:
                ImageData.bad_emotion_count += emot[0]['Confidence']
            n_count += 1

        mydict = {'smile': smile_count,
                  'pose_roll': pose_roll / n,
                  'pose_pitch': pose_pitch / n,
                  'pose_yaw': pose_yaw / n,
                  'good_emotion': good_emotion_count,
                  'bad_emotion': bad_emotion_count}

        return json.dumps(mydict)
