__author__ = 'andreymigalovich'


class HardwareManager():
    AIR_PUMP_PIN = 17
    LED_1_PIN = 17
    LED_2_PIN = 17
    FAN_PIN = 17


    #Happens at the very beginning of the simulation
    #User input needed to start this
    def startSimSequence1(self):
        self.startAirPump()


        #wait for X time TODO


        self.stopAirPump()
        self.startLed1()

        #wait for X time TODO


        self.stopLed1()



    #called after rfid from ball is identified
    def startSimSequence2(self):
        self.startFan()

        self.startLed2()

        #wait for X time TODO


        self.stopLed2()

        #wait for X time TODO

        self.stopFan()



    def startAirPump(self):
         x = 'TODO'

    def stopAirPump(self):
         x = 'TODO'

    def startLed1(self):
        x = 'TODO'

    def stopLed1(self):
        x = 'TODO'

    def startLed2(self):
        x = 'TODO'

    def stopLed2(self):
        x = 'TODO'

    def startFan(self):
        x = 'TODO'
    def stopFan(self):
        x = 'TODO'