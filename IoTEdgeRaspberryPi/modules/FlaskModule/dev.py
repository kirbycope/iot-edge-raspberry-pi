#!/usr/bin/python
from flask import Flask
from flaskblueprint import routes
import os
import socket


def start():
    getDirectoryName
    getHostIp()
    app = Flask(__name__)
    app.register_blueprint(routes)
    app.run(host="0.0.0.0", port=1337, debug=True)

if __name__ == "__main__":
    start()
