#!/usr/bin/python
from flask import Flask
from devblueprint import routes
import os
import socket


def getDirectoryName():
    try:
        os.path.dirname(os.path.realpath(__file__))
        print("dir_path: " + str(dir_path))
    except:
        print("Unable to get Directory")


def getHostIp():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ", host_name)
        print("http://" + host_ip + ":1337")
    except:
        print("Unable to get Hostname and IP")


def start():
    getDirectoryName()
    getHostIp()
    app = Flask(__name__)
    app.register_blueprint(routes)
    app.run(host="0.0.0.0", port=1337, debug=True)

if __name__ == "__main__":
    start()
