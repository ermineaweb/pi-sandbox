# VCC => pin 1 (pin number)
# GND => pin 9
# I/0 => pin 11
import RPi.GPIO as GPIO
from time import sleep

def beepOn(delaySeconds, GPIO, pinNumber):
    GPIO.output(pinNumber, GPIO.LOW)
    sleep(delaySeconds)

def beepOff(delaySeconds, GPIO, pinNumber):
    GPIO.output(pinNumber, GPIO.HIGH)
    sleep(delaySeconds)

pin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
try:
	while True:
		beepOn(0.5, GPIO, pin)
		beepOff(0.5, GPIO, pin)
		
finally:
	GPIO.cleanup()

