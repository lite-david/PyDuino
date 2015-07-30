# pyDuino

The PyDuino project aims to make python interactive with hardware particularly arduino. 

The python interactive terminal can be used to shoot commands to the arduino for quick testing/prototyping. Moreover if a python script is being written which requires hardware interaction, the need can easily be fulfilled. The python library (see pyduino.py) has functions, names kept very short, like dw() for digitalWrite, pm() for pinMode(), parameters given in the same format too, like dw(pin,value) is similar to digitalWrite(pin,value). This makes it a breeze to type, test and debug. There are a few other libraries out there which try to do the similar thing, but this one uses minimum data transfer via the serial connection. 

Function desription and implementation:


dw(pin,value)
	
Equivalent to digitalWrite(pin,value) on arduino. Makes the specified pin, either HIGH or LOW. The function has error detection for wrong pin number and takes only integer values. Value can be either 'HIGH' or 'LOW'. 
