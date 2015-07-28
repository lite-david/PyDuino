import serial
global cw
cw = 1
global ser
ser = serial.Serial('/dev/ttyUSB2',9600)

def dw(pin,value):
	dw_cw_1 = cw << 6 | cw << 5 | cw << 4
	dw_cw_2 = dw_cw_1 | pin
	if ser.isOpen():
		ser.write(chr(dw_cw_2))
		if value == 'HIGH':
			ser.write(chr(dw_cw_1 | 15))
		else:
			ser.write(chr(dw_cw_1))

dw(13,'HIGH')	

