# -*- coding: utf-8 -*-

import time
import signal
import sys

from flask import Flask, request
app = Flask(__name__)

#from zwsgi import monkey
#monkey.patch_all()

from zwsgi.servers import ZMQRouterDealerServer as WSGIServer


@app.route('/ping')
def hello_world():
    """
    channel = request.environ.get('channel')
    while True:
        channel.send_response('hi')
        time.sleep(1)
    """
    return 'Hello World!'


def signal_handler(signal, frame):
	print("Exiting")
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.sleep()

def main():
    server = WSGIServer(('127.0.0.1', 7000), app)
    print server
    server.serve_forever()


if __name__ == "__main__":
    main()
