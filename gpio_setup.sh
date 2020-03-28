#Set which pins are output. wiringpi
gpio mode 0 out
gpio mode 1 out
gpio mode 2 out

#Turn on each LED
gpio write 0 1
gpio write 1 1
gpio write 2 1

