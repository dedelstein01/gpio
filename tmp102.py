import smbus
import time

def getTemp():
	bus = smbus.SMBus(1)
	data = bus.read_i2c_block_data(0x48, 0)
	msb = data[0]
	lsb = data[1]
	cel = (((msb << 8) | lsb) >> 4) * 0.0625 
	far = cel * 1.8 + 32
	return far; 



print getTemp(), time.strftime("%d/%m/%Y - %H:%M:%S")

if getTemp() < 77:
	print("It's cold")
else:
	print("It's hot")
