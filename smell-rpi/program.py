from flask import Flask, request
from HardwareManager import HardwareManager
from LedManager import LedManager
from rfreader.rfreader import RfReaderManager
from manager import Manager
from migutils.LoggerWrapper import LoggerWrapper
import threading

app = Flask(__name__)

airPumpRunning = False
gpioPin = 17
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

def initRfLoop():
    manager = Manager()
    rfreader = RfReaderManager()
    rfreader.register(manager)
    rfreader.startRfLoop()



if __name__ == '__main__':

      #init logger
    logger = LoggerWrapper()
    logger.add_handler()
    initRfLoop()
    #t = threading.Thread(target=initRfLoop)
    #t.start()
    #LedManager.colortrail()
#    app.run(host='0.0.0.0', port=4000, debug=True)
















