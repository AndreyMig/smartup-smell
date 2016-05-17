from flask import Flask, request
from HardwareManager import HardwareManager
from LedManager import LedManager
from rfreader.rfreader import RfReaderManager
from manager import Manager
from migutils.LoggerWrapper import LoggerWrapper
import threading
from server_comm import ServerComm
import time 

app = Flask(__name__)

airPumpRunning = False

hwManager = HardwareManager()
#register to events from rfreader



@app.route('/startseq', methods=['GET'])
def startSeq():
    hwManager.startSimSequence1()
    return 'OK'




# @app.route('/stoptAirPump', methods=['POST'])
# def stoptAirPump():
#    #stop air pump TODO
#     x = 0

def initStartCheckLoop():
    while True:
        logger.info('initStartCheckLoop()')
        json_data = ServerComm.startCheck() 
        if json_data['status'] >= 0:     
            output = json_data['start']
            if int(output) == 1:
                 hwManager.startSimSequence1()
                 time.sleep(5)
        time.sleep(5)

def initRfLoop():
    manager = Manager()
    rfreader = RfReaderManager()
    rfreader.register(manager)
    rfreader.startRfLoop()



if __name__ == '__main__':

      #init logger
    logger = LoggerWrapper()
    logger.add_handler()
   # initRfLoop()

    t1 = threading.Thread(target=initRfLoop)
    t1.start()

    t2 = threading.Thread(target=initStartCheckLoop)
    t2.start()
    #LedManager().blink1_3()
    #app.run(host='0.0.0.0', port=4000, debug=True)
















