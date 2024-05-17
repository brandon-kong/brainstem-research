from utils.logger.Logger import Logger


class LoggerFactory:
    flyweight_loggers = {}

    @staticmethod
    def make_logger(logger_suffix: str, log_file: str, level: str = 'INFO') -> Logger:
        if log_file not in LoggerFactory.flyweight_loggers:
            LoggerFactory.flyweight_loggers[log_file] = Logger(logger_suffix, log_file, level)
        return LoggerFactory.flyweight_loggers[log_file]

    def __init__(self) -> None:
        raise RuntimeError('Cannot instantiate a LoggerFactory object')

    def __new__(cls):
        raise RuntimeError('Cannot instantiate a LoggerFactory object')
