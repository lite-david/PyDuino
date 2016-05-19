#Title: This is a Test designed to test workings of aw#
#Pranaydeep Singh#
#E-mail: theeviltwin@protonmail.com#
#Code for ar last changed: 18th May 2016#

import pyduino
import time
ard = pyduino.arduino('/dev/ttyACM1',9600)
while(1):
    motorvalue=ard.ar(0)
    print('Value from Potentiometer: %d ' % (motorvalue))
    ledvalue=motorvalue//4
    ard.aw(3, ledvalue)
    time.sleep(0.1)
    