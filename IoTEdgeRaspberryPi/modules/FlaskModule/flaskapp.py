#!/usr/bin/python
from flask import Flask
from flaskblueprint import routes
import os
import socket


def start():
    app = Flask(__name__)
    app.register_blueprint(routes)
    app.run(host="0.0.0.0")
