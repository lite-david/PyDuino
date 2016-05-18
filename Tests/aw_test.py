#Title: This is a Test designed to test workings of aw#
#Pranaydeep Singh#
#E-mail: theeviltwin@protonmail.com#
#Code for aw last changed: 18th May 2016#

import pyduino
import time
ard = pyduino.arduino('/dev/ttyACM0',9600)
brightness = 0
while brightness < 255:
    ard.aw(3, brightness)
    ard.aw(5, 255-brightness)
    brightness += 20
    time.sleep(0.01)
