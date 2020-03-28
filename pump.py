import RPi.GPIO as gpio
import time

gpio.setwarnings(True)
gpio.setmode(gpio.BCM)
gpio.setup(5,gpio.OUT)

i = 0
while i < 10:
    gpio.output(5,True)
    time.sleep(1)
    gpio.output(5,False)
    time.sleep(1)
    i += 1
