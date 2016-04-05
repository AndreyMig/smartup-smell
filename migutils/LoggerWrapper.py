import logging


class LoggerWrapper:

    DEF_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoggerWrapper, cls).__new__(cls, *args)
            cls._instance.logger = logging.getLogger(__name__)
            cls._instance.logger.setLevel(logging.DEBUG)
            consoleHandler = logging.StreamHandler()
            logFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            consoleHandler.setFormatter(logFormatter)
            cls._instance.logger.addHandler(consoleHandler)
        return cls._instance


    def __init__(self):
        if not LoggerWrapper._instance:
            LoggerWrapper._instance = LoggerWrapper()


    def info(self, msg):
        self.logger.info(msg.encode('utf-8'))


    def error(self, msg):
        self.logger.error(msg.encode('utf-8'))


    def add_handler(self, file_name = 'notifier_log.log',
                    format = DEF_FORMAT,
                    log_level = logging.DEBUG):
        handler = logging.FileHandler(file_name)
        self.logger.setLevel(log_level)
        formatter = logging.Formatter(format)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

