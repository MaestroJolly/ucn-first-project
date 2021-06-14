import json
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def status():
    status = {
        'result': 'OK - healthy'
    }
    return json.dumps(status)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
