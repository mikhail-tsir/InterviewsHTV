from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'INDEX'

@app.route('/retrievejson')
def index():
    return 'It works'

if __name__ == '__main__':
    app.run(debug=True)