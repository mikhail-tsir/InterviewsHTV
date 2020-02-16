import numpy.random
import json

numpy.random.seed(0)

def givetips(data):

    #smile, roll, pitch, yaw, good
    smile = data['smile']
    roll = data['pose_roll']
    pitch = data['pose_pitch']
    yaw = data['pose_yaw']
    good = data['good_emotion']
    tips = ""
    rand = 0
    print("Smile is " + str(smile))
    print("Roll is " + str(roll))
    print("Pitch is " + str(pitch))
    print("yaw is " + str(yaw))
    print("good is " + str(good))
    if (smile <= 0):
        rand = numpy.random.randint(0,3)
        if (rand == 0):
            tips = tips + ("Try to smile more! ")
        elif (rand == 1):
            tips = tips + ("Show those teeth! ")
        elif (rand == 2):
            tips = tips + ("Smiling makes you appear friendlier! ")
        else:
            tips = tips + ("Try to loosen up! ")
    if (roll > 30 or pitch > 30 or yaw > 30):
        tips = tips + ("Make sure you face the interviewer! ")
    if (good < 0):
        tips = tips + ("Relax a little bit, you look stressed! ")
    return json.dumps(tips)

