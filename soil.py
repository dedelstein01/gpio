import RPi.GPIO as gpio
import time

gpio.setwarnings(True)
gpio.setmode(gpio.BCM)
gpio.setup(5,gpio.OUT)
gpio.setup(21,gpio.IN)

while True:
    if gpio.input(21):
        print gpio.input(21)
        gpio.output(5,True)
        time.sleep(1)
        gpio.output(5,False)
        time.sleep(10)
    else:
        print gpio.input(21)
        time.sleep(10)

