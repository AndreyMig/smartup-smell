from HardwareManager import HardwareManager
from observer import Observer
from server_comm import ServerComm
from migutils.LoggerWrapper import LoggerWrapper
import time
import json

class Manager(Observer):

    def __init__(self):
        self.hardwareManager = HardwareManager()
        self.logger = LoggerWrapper()


    def update(self, *args, **kwargs):
        #print("Params from rf: {0}".format(args))
        rfid = args[0]
        self.logger.info('rf recievied: ' + rfid)
        self.sendRfAndProcessResponse(rfid)
        time.sleep(0.5)
        self.hardwareManager.startSimSequence2()
        time.sleep(0.5)
        




    def sendRfAndProcessResponse(self, rfid):
        json_data = ServerComm.sendRfId(rfid) 
        if json_data['status'] > -1:     
            output = json_data['smell_data']['output_id']
            self.hardwareManager.startOutputSequence(output)
        else:
            print("SERVER DID NOT RECOGNIZE RFID: " + str(rfid))


