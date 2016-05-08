import urllib.request

SERVER_HOST = "172.20.18.178"
SERVER_PORT = 3000
class ServerComm():


    def sendRfId(rfid):
        url = "http://" + SERVER_HOST +":" + str(SERVER_PORT) + "/rf?rfid="+rfid
        print("sending request to " + url)
        response = urllib.request.urlopen(url)
        json = response.read()
        print('res from server' + str(json))
        return json






