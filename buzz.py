# VCC => pin 1 (pin number)
# GND => pin 9
# I/0 => pin 11
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
try:
	while True:
		print("Beep ON")
		GPIO.output(11, GPIO.LOW)
		sleep(0.2)

		print("Beep OFF")
		GPIO.output(11, GPIO.HIGH)
		sleep(0.6)
		
finally:
	GPIO.cleanup()