from .Logger import Logger

class LoggerFactory:

    flyweight_loggers = {}

    @staticmethod
    def make_logger(log_file: str) -> Logger:
        if log_file not in LoggerFactory.flyweight_loggers:
            LoggerFactory.flyweight_loggers[log_file] = Logger(log_file)
        return LoggerFactory.flyweight_loggers[log_file]
    
    def __init__(self) -> None:
        raise RuntimeError('Cannot instantiate a LoggerFactory object')
    
    def __new__(cls):
        raise RuntimeError('Cannot instantiate a LoggerFactory object')