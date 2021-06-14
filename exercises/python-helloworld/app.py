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


@app.route("/metrics")
def metrics():
    metrics = {
        'data': {'UserCount': 140, 'UserCountActive': 23}
    }
    return json.dumps(metrics)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
