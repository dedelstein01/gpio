import smbus
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # use BCM pin numbering
GPIO.setwarnings(True)
gpio_pin_number = 12
GPIO.setup(gpio_pin_number, GPIO.OUT) # mark for output


def getTemp():
	bus = smbus.SMBus(1)
	data = bus.read_i2c_block_data(0x48, 0)
	msb = data[0]
	lsb = data[1]
	cel = (((msb << 8) | lsb) >> 4) * 0.0625 
	far = cel * 1.8 + 32
	return far; 



while True:
	if getTemp() < 72:
		print getTemp(), time.strftime("%d/%m/%Y - %H:%M:%S")
		print("It's cold")
		GPIO.output(gpio_pin_number, GPIO.HIGH)
		time.sleep(30)
	if getTemp() > 74:
		print getTemp(), time.strftime("%d/%m/%Y - %H:%M:%S")
		print("It's hot")
		GPIO.output(gpio_pin_number, GPIO.LOW)
		time.sleep(30)
	else:
		print getTemp(), time.strftime("%d/%m/%Y - %H:%M:%S")
		time.sleep(30)


GPIO.cleanup()
	
