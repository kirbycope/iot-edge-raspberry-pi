#!/usr/bin/python
from flask import Flask
from flaskpackage.flaskblueprint import routes
import os
import socket


def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ", host_name)
        print("http://" + host_ip + ":5000")
    except:
        print("Unable to get Hostname and IP")


def start():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(str(dir_path))
    get_Host_name_IP()
    app = Flask("flaskapp")
    from . import flaskblueprint
    app.register_blueprint(routes)
    try:
        app.run(host="0.0.0.0")
    except RunTimeError as rte:
        print(str(rte))
        raise rte
