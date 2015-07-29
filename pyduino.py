'''
PyDuino python library for using arduino based functions from python
Via serial connection between hardware and PC 
Check arduino.ino for functions to be added on the arduino

by Edwin Mascarenhas 
edwin.mascarenhas95@gmail.com
'''
import serial
global cw
cw = 1
global ser
ser = serial.Serial('/dev/ttyUSB0',9600)

def dw(pin,value):
	if(pin > 13 or pin < 0 or type(pin).__name__ != "int"):
		print "Error: Incorrect pin value"
		return False 
	elif(value is not "HIGH"):
		if(value is not "LOW"):
			print "Error: Value can be either HIGH or LOW"
			return False
	dw_cw_1 = cw << 6 | cw << 5 | cw << 4
	dw_cw_2 = dw_cw_1 | pin
	if ser.isOpen():
		ser.write(chr(dw_cw_2))
		if value == 'HIGH':
			ser.write(chr(dw_cw_1 | 15))
			return True
		elif value == 'LOW':
			ser.write(chr(dw_cw_1))
			return True
		else:
			print "Error: Can't access device file"
			return False

def dr(pin):
	if(pin > 13 or pin < 0 or type(pin).__name__ != "int"):
		print "Error: Incorrect pin value"
		return False
	dr_cw_1 = cw << 6 | cw << 5 | pin
	if ser.isOpen():
		ser.write(chr(dr_cw_1))
		print ser.read()
		return True
	else:
		print "Error: Can't access device file"
		return False
	

def pm(pin,mode):
	if(pin > 13 or pin < 0 or type(pin).__name__ != "int"):
		print "Error: Incorrect pin value"
		return False
	elif(mode != 'OUTPUT' and mode != 'INPUT'):
		print "Error: Invalid mode"
		return False
	if(mode == 'INPUT'):	
		pm_cw_1 = cw  << 5 | pin 
		flag = ser.write(chr(pm_cw_1))
		return True if flag else False
	elif(mode == 'OUTPUT'):
		pm_cw_1 = cw  << 5 | pin | cw << 4
		flag = ser.write(chr(pm_cw_1))
		return True if flag else False
		

pm(12,'INPUT')
pm(13,'OUTPUT')
dw(13,'HIGH')
dr(12)