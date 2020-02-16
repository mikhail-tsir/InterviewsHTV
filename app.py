from flask import Flask
import __main__


app = Flask(__name__)


@app.route('/')
def index():
    return 'more'
if __name__ == '__main__':
    app.run(debug=True)
