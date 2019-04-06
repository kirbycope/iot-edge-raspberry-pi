#!/usr/bin/python
import RPi.GPIO as GPIO
import time

PinList = [10, 9, 11, 5, 6, 13, 19, 26, 24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setmode(GPIO.BCM)

def GetState(pinNumber):
    state = 0
    try:
        state = GPIO.input(pinNumber)
    except RuntimeError as ex:
        print(str(ex))
    return state

def TogglePin(pinNumber, sleepSeconds=0):
    state = GetState(pinNumber)
    if (state == 0):
        state = TurnOnPin(pinNumber)
    else:
        state = TurnOffPin(pinNumber)
    time.sleep(sleepSeconds)
    return state

def TurnOffPin(pinNumber, sleepSeconds=0):
    GPIO.output(pinNumber, GPIO.LOW)
    time.sleep(sleepSeconds)
    return GetState(pinNumber)
    
def TurnOffPins(pinList, sleepSeconds=0):
    for pinNumber in pinList:
        TurnOffPin(pinNumber, sleepSeconds)
        time.sleep(sleepSeconds)

def TurnOnPin(pinNumber, sleepSeconds=0):
    GPIO.setup(pinNumber, GPIO.OUT)
    GPIO.output(pinNumber, GPIO.HIGH)
    time.sleep(sleepSeconds)
    return GetState(pinNumber)

def TurnOnPins(pinList, sleepSeconds=0):
    for pinNumber in pinList:
        TurnOnPin(pinNumber, sleepSeconds)

def Cleanup():
    GPIO.cleanup()
