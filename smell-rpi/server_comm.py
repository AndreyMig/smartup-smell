import urllib.request
import codecs
import json
import sys
SERVER_HOST = "smellapp.tk" if len(sys.argv) <= 1 else sys.argv[1]
SERVER_PORT = 80
class ServerComm():


    def sendRfId(rfid):
        url = "http://" + SERVER_HOST +":" + str(SERVER_PORT) + "/rf?rfid="+rfid
        print("sending request to " + url)
        response = urllib.request.urlopen(url)
        encoding = response.info().get_content_charset('utf8')
        data = json.loads(response.read().decode(encoding))
        #res = response.read().decode('utf-8')
        #obj = json.load(res)
        print('res from server' + str(data))
        return data

    def startCheck():
        url = "http://" + SERVER_HOST +":" + str(SERVER_PORT) + "/startcheck"
        print("sending request to " + url)
        response = urllib.request.urlopen(url)
        encoding = response.info().get_content_charset('utf8')
        data = json.loads(response.read().decode(encoding))
        #res = response.read().decode('utf-8')
        #obj = json.load(res)
        print('res from server' + str(data))
        return data






