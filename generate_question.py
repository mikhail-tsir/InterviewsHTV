import json
import numpy.random


numpy.random.seed(0)

def gen_q():
    with open('interview-questions.json') as json_file:
        data = json.load(json_file)
        #print(data)
        n = numpy.random.randint(1, 14)
        number = str(n)
        print(data[number]['text'])
        return (data[number]['text'])
