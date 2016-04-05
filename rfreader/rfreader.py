from observable import Observable
import serial
import binascii
import RPi.GPIO as GPIO
import time

class RfReaderManager(Observable):
	#def _init_(self):
	#	self.RESET_PIN = 23
	def startRfLoop(self):
		ser = serial.Serial("/dev/ttyS0")
		ser.baudrate = 9600

		while True:
			#self.resetReader()
			d1 = ser.read(11)
			data = str(binascii.hexlify(d1))[2:24] 
			print(data)
			self.update_observers(data)

		ser.close()
	def resetReader(self):
		print('reseting reader')
		RESET_PIN = 23
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(RESET_PIN, GPIO.OUT)
		GPIO.output(RESET_PIN, GPIO.LOW)	
		GPIO.output(RESET_PIN, GPIO.HIGH)
		time.sleep(1)
		print('READER WAS RESET')




