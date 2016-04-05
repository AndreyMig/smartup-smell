from flask import Flask, request
from HardwareManager import HardwareManager
from rfreader.rfreader import RfReaderManager
from manager import Manager
from migutils.LoggerWrapper import LoggerWrapper

app = Flask(__name__)

airPumpRunning = False
gpioPin = 17
hwManager = HardwareManager()
#register to events from rfreader



@app.route('/startSeq', methods=['POST'])
def startSeq():
    hwManager.startSimSequence1()
    return 'OK'




# @app.route('/stoptAirPump', methods=['POST'])
# def stoptAirPump():
#    #stop air pump TODO
#     x = 0



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)

    #init logger
    logger = LoggerWrapper()
    logger.add_handler()

    manager = Manager()
    rfreader = RfReaderManager()
    rfreader.register(manager)














