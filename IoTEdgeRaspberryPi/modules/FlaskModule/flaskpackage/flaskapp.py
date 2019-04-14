#!/usr/bin/python
from flask import Flask
from flaskpackage.flaskblueprint import routes
import os
import socket
from . import flaskblueprint


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
        print("http://" + host_ip + ":5000")
    except:
        print("Unable to get Hostname and IP")


def start():
    getDirectoryName
    getHostIp()
    app = Flask(__name__, root_path="/app/flaskpackage")
    app.register_blueprint(routes)
    try:
        app.run(host="0.0.0.0")
    except RunTimeError as rte:
        print(str(rte))