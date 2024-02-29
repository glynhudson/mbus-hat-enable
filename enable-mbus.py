#! /usr/bin/python3

print('Enabling MBUS...')

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

mbuspin = 26

GPIO.setup(mbuspin, GPIO.OUT)

GPIO.output(mbuspin, 1)


