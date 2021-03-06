
from migutils.LoggerWrapper import LoggerWrapper
import RPi.GPIO as GPIO
import time
import threading
from LedManager import LedManager

class HardwareManager():

    AIR_PUMP_PIN = 38 #green relay coord
    LED_1_PIN = 32
    LED_2_PIN = 36
    FAN_PIN = 40 #grey relay coord
	
    OUTPUT_DIR_PIN = 29

    BIN_PINS = [31, 33, 35, 37] # msb left to right


    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.logger = LoggerWrapper()
        self.flag = 0

		#reset all GPIO functions
        self.stopFan()
        self.stopAirPump()
        self.outputBinaryPins([0, 0, 0, 0])
        self.setOutputDir(GPIO.LOW)
        time.sleep(0.5)
        self.outputBinaryPins([0, 0, 0, 0])

    #Happens at the very beginning of the simulation
    #User input needed to start this
    def startSimSequence1(self):
        self.logger.info("startSimSequence1()")
        t = threading.Thread(target=self.startSim1)
        t.start()

    def startOutputSequence(self, output_id):
        self.logger.info("startOutputSequence()")
        #t = threading.Thread(target=self.startOutputSeq)
        #t.start()
        self.output(output_id)


    def output(self, id):
        self.logger.info("output()")

        #reset all binary pins
        self.setOutputDir(GPIO.LOW)
        self.outputBinaryPins([0, 0, 0, 0])


        binary = "{0:010b}".format(int(id))
        binarylist = list(binary)[6:]
        self.logger.info(str(id) + " in binary: " + str(binarylist))

        #set dir to 0

        self.outputBinaryPins(binarylist)
        self.setOutputDir(GPIO.LOW)
        time.sleep(1)
        self.setOutputDir(GPIO.HIGH)
        time.sleep(2)
        self.setOutputDir(GPIO.LOW)
        time.sleep(1)
        self.outputBinaryPins([0, 0, 0, 0])




    def outputBinaryPins(self, binarynum):
        self.logger.info("outputBinaryPins()")
        for idx, bit in enumerate(binarynum):
            bit = int(bit)
            self.logger.info(str(idx) +' bit is '+str(bit))
            GPIO.setup(HardwareManager.BIN_PINS[idx], GPIO.OUT)
            if bit == 1:
                print(str(HardwareManager.BIN_PINS[idx]) + "  high")
                GPIO.output(HardwareManager.BIN_PINS[idx], GPIO.HIGH)
            elif bit == 0:
                print(str(HardwareManager.BIN_PINS[idx]) + "   low")
                GPIO.output(HardwareManager.BIN_PINS[idx], GPIO.LOW)

    def setOutputDir(self, dir):
        self.logger.info("setOutputDir()")
        GPIO.setup(HardwareManager.OUTPUT_DIR_PIN, GPIO.OUT)
        GPIO.output(HardwareManager.OUTPUT_DIR_PIN, dir)


    #def startOutputSeq(self):
     #   self.outPut

    def startSim1(self):
        self.logger.info("thread started for: startSim1()")
        self.startAirPump()
        time.sleep(3)
        self.stopAirPump()
        time.sleep(0.5)
        self.startLed1()
        time.sleep(1)
        self.stopLed1()
        t = threading.Thread(target=self.takpiz())
        t.start()


    def takpiz(self):
        while self.flag == 0:
            self.startAirPump()
            time.sleep(0.2)
            self.stopAirPump()
            time.sleep(0.2)
        self.stopAirPump()

    #called after rfid from ball is identified
    def startSimSequence2(self):
        self.logger.info("startSimSequence2()")
        self.flag = 1
        time.sleep(0.5)
        t = threading.Thread(target=self.startSim2)
        t.start()


    def startSim2(self):
        self.logger.info("thread started for: startSim2()")
        self.startFan()
        self.startLed1()
        time.sleep(2)
        self.stopLed2()
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
        # LedManager.colortrail();
        GPIO.setup(HardwareManager.LED_1_PIN, GPIO.OUT)
        GPIO.output(HardwareManager.LED_1_PIN, GPIO.HIGH)


    def stopLed1(self):
       self.logger.info("stopLed1()")
       GPIO.setup(HardwareManager.LED_1_PIN, GPIO.OUT)
       GPIO.output(HardwareManager.LED_1_PIN, GPIO.LOW)

    def startLed2(self):
       self.logger.info("startLed2()")
        # LedManager.colortrail2();
       GPIO.setup(HardwareManager.LED_2_PIN, GPIO.OUT)
       GPIO.output(HardwareManager.LED_2_PIN, GPIO.HIGH)

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
