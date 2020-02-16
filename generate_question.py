import json
from numpy.random import seed
from numpy.random import randint


def gen_q():
    seed(1)
    with open('interview-questions.json') as json_file:
        data = json.load(json_file)
        print(data)
        n = randint(1, 14)
        number = str(n)
        print(data[number]['text'])
        return (data[number]['text'])
