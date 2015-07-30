# PyDuino

##Introducing the PyDuino

The PyDuino project aims to make python interactive with hardware particularly arduino. 

The python interactive terminal can be used to shoot commands to the arduino for quick testing/prototyping. Moreover if a python script is being written which requires hardware interaction, the need can easily be fulfilled. The python library (see pyduino.py) has functions, names kept very short, like dw() for digitalWrite, pm() for pinMode(), parameters given in the same format too, like dw(pin,value) is similar to digitalWrite(pin,value). This makes it a breeze to type, test and debug. There are a few other libraries out there which try to do the similar thing, but this one uses minimum data transfer via the serial connection. 

##Under the hood

A byte of data is being sent on the serial communication, using the PySerial python library. However with every serial.write(), the an ASCII character is being sent. So on writing serial.write("99"), arduino reads it as two seperate characters 9 and 9. However each ASCII character has an equivalent decimal number or rather 0 - 256 decimal numbers, ie an 8 bit number has an equivalent ASCII character. I have exploited this property, to encode function information bitwise in a number and send it as an ASCII character over the serial connection, which is just 1 byte long and then decode it at the arduino end.

The encoding method I have used is:

7th bit - 0 

if 6th bit - 1 : Implements digitalRead(), digitalWrite(), analogRead(), analogWrite()				       
5th bit - 1 if digital, 0 if analog                                                                                    
4th bit - 1 if write, 0 if read                                                                                        
3rd - 0th bit - Pin number                                                                                             

if 6th bit - 0 : Implements pinMode() function                                                                        
5th bit -1                                             								
4th bit - 0 if input, 1 if output 										
3rd bit - 0th bit - Pin number											

##Function Description

####dw(pin,value)
	
Equivalent to digitalWrite(pin,value) on arduino. Makes the specified pin, either HIGH or LOW. The function has error detection for wrong pin number and takes only integer values. Value can be either 'HIGH' or 'LOW'. Sends two bytes of data over the serial line, 1st byte according to the information above. Second byte to indicate whether 'HIGH' or 'LOW'
The format for second byte is, bits 7,6,5,4 remain same. If 3rd - 0th bit are 0's then 'LOW'. If 3rd - 0th bit all 1's then 'HIGH'.
Useage: 
dw(13,'HIGH')
sets pin 13 high, ie 3.3V or 5V 
The function has been tested and it works.

####dr(pin)

Equivalent to digitalRead(pin) on arduino. Reads the value on the specified pin and prints it on the python terminal. Function is yet to be entirely tested. Has worked for certain cases.

####pm(pin,mode)

Equivalent to pinMode(pin,value) on arduino. Sets specified pin as input or output. The function has been tested and works correctly. Mode can be either 'INPUT' or 'OUTPUT'
Useage:
pm(13,'INPUT')
Sets pin 13 as input

####delay(millisecs)

Equivalent to delay(millisecs) function on arduino. Pauses the python interpreter for the specified time. Utilizes python's time library. Note, here time is to be specified in milliseconds and not in seconds.
Useage:
delay(1000)
This gives a 1 second delay.

## Future work

-- Adding analog functions
-- Arduino header file, which can be included rather than cluttering code
-- optimizing python code to improve speed. Often there is a time sync issue between arduino and python. For example, in the arduino code for dw, I have put a 2 millisec delay because without that, python had not sent the second byte of data, and by then arduino had already looped over and so it took the second byte of data, ie the control word specifying high or low as the control word which specifies pin number. The issue is mainly because, python is interpreted rather than C/C++ or the code which is running on arduino which is all machine code. Moreover while the python execution is going on, there are other processes running on your OS and so this multi-threading puts a certain delay too.
-- Adding custom functions and database functionality. It helps if there is a database,where large number of sensor values from arduino can be stored. 

## Contact

For any other queries regarding the code, contact me at: edwin.mascarenhas95@gmail.com
