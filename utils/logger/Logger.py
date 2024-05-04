# This file contains the Logger class which is used to log messages to a file.
# The class has three methods:
# - log: Logs a message to the file
# - read: Reads the contents of the log file
# - clear: Clears the contents of the log file

import os
from datetime import datetime

from utils.FileUtility import FileUtility

from utils.constants import LOGGER_FILE_SUFFIX

class Logger:
    """
    The Logger class is a singleton class that logs messages to a file.
    """
    LEVELS = {
        'DEBUG': 0,
        'INFO': 1,
        'WARNING': 2,
        'ERROR': 3,
        'CRITICAL': 4
    }
    
    def __init__(self, logger_suffix: str, log_file: str, level: str = 'INFO'):

        # Check if the log file has the correct suffix
        if not log_file.endswith(logger_suffix):
            raise ValueError('Log file must have the correct suffix')
        
        self.log_file = log_file
        self.level = self.LEVELS.get(level.upper(), 'INFO')
        
        # Check if the log file exists
        if not os.path.exists(log_file):
            FileUtility.create_file(log_file)

    def log(self, message: str, level: str = 'INFO'):

        # get the current time
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if self.LEVELS[level] >= self.level:
            with open(self.log_file, 'a') as f:
                f.write(f'{time} {level}: {message}\n')

    def error(self, message: str):
        self.log(f'{message}', level='ERROR')

    def info(self, message: str):
        self.log(f'{message}', level='INFO')

    def warning(self, message: str):
        self.log(f'{message}', level='WARNING')

    def debug(self, message: str):
        self.log(f'{message}', level='DEBUG')

    def critical(self, message: str):
        self.log(f'{message}', level='CRITICAL')

    def read(self):
        # make sure the file exists
        if not self.file_exists():
            raise FileNotFoundError('Log file does not exist')
        
        with open(self.log_file, 'r') as f:
            return f.read()
        
    def clear(self):
        with open(self.log_file, 'w') as f:
            f.write('')

    def delete(self):
        if self.file_exists():
            os.remove(self.log_file)

    def file_exists(self):
        return os.path.exists(self.log_file)

