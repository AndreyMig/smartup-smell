import urllib.request

SERVER_HOST = "127.0.0.1"

class ServerComm():


    def sendRfId(rfid):
        response = urllib.request.urlopen("http://" + SERVER_HOST + "/rf?rfid="+rfid)
        json = response.read()
        return json






