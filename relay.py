#initialization
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # use BCM pin numbering
GPIO.setwarnings(True)
gpio_pin_number = 12
GPIO.setup(gpio_pin_number, GPIO.OUT) # mark for output
 
#end of initialization; following could be called multiple times.

for i in range (0, 3): 
	GPIO.output(gpio_pin_number, GPIO.HIGH) # output high / 3.3v
	print("high")
	time.sleep(3)
	GPIO.output(gpio_pin_number, GPIO.LOW) # output low / 0v
	print("low")
	time.sleep(3)

GPIO.cleanup()
