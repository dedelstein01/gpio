#!/usr/bin/python
print('Content-type: text/html\r\n\r')
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

x = 3

while (x>0):
	print "LED on"
	GPIO.output(17,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(18, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(27, GPIO.HIGH)
	time.sleep(0.5)
	print "LED off"
	GPIO.output(17, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)
	time.sleep(1)
	i = 0;	
	for i in range(0, 10):
		GPIO.output(17, GPIO.HIGH)
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		time.sleep(0.25)
		GPIO.output(17, GPIO.LOW)
		GPIO.output(18, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		time.sleep(0.25)
	
	x -= 1
