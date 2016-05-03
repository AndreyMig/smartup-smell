
import RPi.GPIO as GPIO
import time
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.HIGH)
time.sleep(4)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)


