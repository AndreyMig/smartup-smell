from HardwareManager import HardwareManager
from observer import Observer
from server_comm import ServerComm

class Manager(Observer):

    def __init__(self):
        self.hardwareManager = HardwareManager()



    def update(self, *args, **kwargs):
        print("American stock market received: {0}\n{1}".format(args, kwargs))
        rfid = 'TODO'
        self.hardwareManager.startSimSequence2()
        self.sendRfAndProcessResponse(rfid)




    def sendRfAndProcessResponse(self, rfid):
        json = ServerComm.sendRfId(rfid)


