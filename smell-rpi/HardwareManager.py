
from migutils.LoggerWrapper import LoggerWrapper
import RPi.GPIO as GPIO
import time
import threading
from LedManager import LedManager

class HardwareManager():

    AIR_PUMP_PIN = 38 #green relay coord
    LED_1_PIN = 12
    LED_2_PIN = 16
    FAN_PIN = 40 #grey relay coord

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.logger = LoggerWrapper()

    #Happens at the very beginning of the simulation
    #User input needed to start this
    def startSimSequence1(self):
        self.logger.info("startSimSequence1()")
        t = threading.Thread(target=self.startSim1)
        t.start()




    def startSim1(self):
        self.logger.info("thread started for: startSim1()")
        self.startAirPump()
        time.sleep(4)
        self.stopAirPump()
        self.startLed1()
        #time.sleep(1)
        #self.stopLed1()



    #called after rfid from ball is identified
    def startSimSequence2(self):
        self.logger.info("startSimSequence2()")
        t = threading.Thread(target=self.startSim2)
        t.start()


    def startSim2(self):
        self.logger.info("thread started for: startSim2()")
        self.startFan()

		#TODO change to led2
        self.startLed1()
        #time.sleep(1)
        #self.stopLed2()

        time.sleep(1)

        self.stopFan()


    def startAirPump(self):
        self.logger.info("startAirPump()")
        GPIO.setup(HardwareManager.AIR_PUMP_PIN, GPIO.OUT)
        GPIO.output(HardwareManager.AIR_PUMP_PIN, GPIO.HIGH)


    def stopAirPump(self):
        self.logger.info("stopAirPump()")
        GPIO.setup(HardwareManager.AIR_PUMP_PIN, GPIO.OUT)
        GPIO.output(HardwareManager.AIR_PUMP_PIN, GPIO.LOW)


    def startLed1(self):
        self.logger.info("startLed1()")
        LedManager.colortrail();
        #GPIO.setup(HardwareManager.LED_1_PIN, GPIO.OUT)
        #GPIO.output(HardwareManager.LED_1_PIN, GPIO.HIGH)

   # def stopLed1(self):
     #   self.logger.info("stopLed1()")
    #    GPIO.setup(HardwareManager.LED_1_PIN, GPIO.OUT)
     #   GPIO.output(HardwareManager.LED_1_PIN, GPIO.LOW)

    def startLed2(self):
        self.logger.info("startLed2()")
        LedManager.colortrail2();
#        GPIO.setup(HardwareManager.LED_2_PIN, GPIO.OUT)
 #       GPIO.output(HardwareManager.LED_2_PIN, GPIO.HIGH)

    def stopLed2(self):
        self.logger.info("stopLed2()")
        GPIO.setup(HardwareManager.LED_2_PIN, GPIO.OUT)
        GPIO.output(HardwareManager.LED_2_PIN, GPIO.LOW)

    def startFan(self):
        self.logger.info("startFan()")
        GPIO.setup(HardwareManager.FAN_PIN, GPIO.OUT)
        GPIO.output(HardwareManager.FAN_PIN, GPIO.HIGH)

    def stopFan(self):
        self.logger.info("stopFan()")
        GPIO.setup(HardwareManager.FAN_PIN, GPIO.OUT)
        GPIO.output(HardwareManager.FAN_PIN, GPIO.LOW)
