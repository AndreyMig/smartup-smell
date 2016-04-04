from .observable import Observable

class RfReaderManager(Observable):

   def startRfLoop(self):

       while True:
           x = 1