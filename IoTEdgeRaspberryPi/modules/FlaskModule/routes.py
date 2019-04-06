#!/usr/bin/python
from flask import Blueprint, jsonify, render_template, request
import rpigpiohelper as RpiGpioHelper
import rpigpiotest as RpiGpioTest

# Define the Blueprint for Flask
routes = Blueprint('routes', __name__)

# GET: "/"
@routes.route("/")
def main():
    return render_template('home.html')

# GET: "/pulse/<pinNumber>"
@routes.route("/pulse/<pinNumber>")
def PulsePin(pinNumber):
    state = RpiGpioHelper.TurnOnPin(int(pinNumber), .2)
    state = RpiGpioHelper.TurnOffPin(int(pinNumber))
    return 'State: ' + str(state)

# GET: "/status"
@routes.route("/status")
def GetStatus():
    jsonObject = []
    for pinNumber in RpiGpioTest.pinList:
        state = RpiGpioHelper.GetState(int(pinNumber))
        jsonObject.append({"pinNumber":pinNumber, "state":state})
    return jsonify(jsonObject)

# GET: "/status/<pinNumber>"
@routes.route("/status/<pinNumber>")
def GetStatusForPin(pinNumber):
    state = RpiGpioHelper.GetState(int(pinNumber))
    return jsonify({'pinNumber': pinNumber, 'state': state})

# GET: "/toggle/<pinNumber>"
@routes.route("/toggle/<pinNumber>")
def TogglePin(pinNumber):
    state = RpiGpioHelper.TogglePin(int(pinNumber))
    return jsonify({'pinNumber': pinNumber, 'state': state})

# GET: "/turnoff/<pinNumber>"
@routes.route("/turnoff/<pinNumber>")
def TurnOffPin(pinNumber):
    state = RpiGpioHelper.TurnOffPin(int(pinNumber))
    return jsonify({'pinNumber': pinNumber, 'state': state})

# GET: "/turnon/<PinNumber>"
@routes.route("/turnon/<pinNumber>")
def TurnOnPin(pinNumber):
    state = RpiGpioHelper.TurnOnPin(int(pinNumber))
    return jsonify({'pinNumber': pinNumber, 'state': state})

# POST: "/shutdown"
@routes.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    RpiGpioHelper.Cleanup()
    return 'Server shutting down...'

# Define the server's shutdown procedure
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
