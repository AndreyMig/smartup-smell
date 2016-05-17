from .observable import Observable
import serial
import binascii
import RPi.GPIO as GPIO
import time
from migutils.LoggerWrapper import LoggerWrapper

class RfReaderManager(Observable):
    def __init__(self):
        print('helleoo')
        super(RfReaderManager, self).__init__()
        self.logger = LoggerWrapper()
	#	self.RESET_PIN = 23
    def startRfLoop(self):
        self.logger.info('starting rf reader loop')
        ser = serial.Serial("/dev/ttyS0")
        ser.baudrate = 9600

        while True:
            self.logger.info('waiting for rf tag')
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
        time.sleep(1)
        GPIO.output(RESET_PIN, GPIO.HIGH)
        print('READER WAS RESET')




