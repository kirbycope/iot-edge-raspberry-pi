#!/usr/bin/python
import  rpigpiohelper as RpiGpioHelper

# Print the status
print("Running...")

# Define the list of pins
pinList = [10, 9, 11, 5, 6, 13, 19, 26, 24, 25, 8, 7, 12, 16, 20, 21]

# Print the status
print("Turning on output devices [at once]...")

# Turn on all the pins in the list
RpiGpioHelper.TurnOnPins(pinList, 0)

# Print the status
print("Turning off output devices [in sequence]...")

# Turn on the pin
RpiGpioHelper.TurnOffPins(pinList, .5)

# Print the status
print("Finished!")

# Reset GPIO settings
RpiGpioHelper.Cleanup()
