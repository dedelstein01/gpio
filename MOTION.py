import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.IN)


while(True):
	if GPIO.input(22):
		print "Motion detected", (time.strftime("%d/%m/%Y")), (time.strftime("%H:%M:%S"))
		
		for i in range(0, 3):
			GPIO.output(17, GPIO.HIGH)
			GPIO.output(18, GPIO.HIGH)
			GPIO.output(27, GPIO.HIGH)
			time.sleep(0.25)
			GPIO.output(17, GPIO.LOW)
			GPIO.output(18, GPIO.LOW)
			GPIO.output(27, GPIO.LOW)
			time.sleep(0.25)

