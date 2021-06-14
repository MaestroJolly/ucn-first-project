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
    response = app.response_class(
        response=json.dumps(status),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/metrics")
def metrics():
    metrics = {
        'success': 'status',
        'code': 0,
        'data': {'UserCount': 140, 'UserCountActive': 23}
    }
    response = app.response_class(
        response=json.dumps(metrics),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
