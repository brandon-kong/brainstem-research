# This file contains the Logger class which is used to log messages to a file.
# The class has three methods:
# - log: Logs a message to the file
# - read: Reads the contents of the log file
# - clear: Clears the contents of the log file

import os

log_file_suffix = '.log.txt'

class Logger:
    """
    The Logger class is a singleton class that logs messages to a file.
    """
    
    def __init__(self, log_file: str):

        # Check if the log file has the correct suffix
        if not log_file.endswith(log_file_suffix):
            raise ValueError('Log file must have the correct suffix')
        
        self.log_file = log_file
        
        # Check if the log file exists
        if not os.path.exists(log_file):
            self.create_file()

    def log(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')

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
    
    def create_file(self):
        if not self.file_exists():
            with open(self.log_file, 'w') as f:
                f.write('')
