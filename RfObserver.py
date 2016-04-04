from observer import Observer
from server_comm import ServerComm

class RFObserver(Observer):


    def update(self, *args, **kwargs):
        print("American stock market received: {0}\n{1}".format(args, kwargs))
        rfid = 'TODO'
        self.sendRfAndProcessResponse(rfid)




    def sendRfAndProcessResponse(self, rfid):
        json = ServerComm.sendRfId(rfid)



