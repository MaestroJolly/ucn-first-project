import json
from flask import Flask
import logging
import datetime
app = Flask(__name__)


@app.route("/")
def hello():
    timestamp = datetime.datetime.now()
    app.logger.info('%s, main endpoint was reached' % timestamp)
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
    timestamp = datetime.datetime.now()
    app.logger.info('%s, status endpoint was reached' % timestamp)
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

    timestamp = datetime.datetime.now()
    app.logger.info('%s, metrics endpoint was reached' % timestamp)
    return response


if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
