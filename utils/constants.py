from typing import Union, Dict, Type, TypedDict

# TYPES

type JSONable = Union[str, int, float, bool, None, Dict[str, JSONable]]

# GENERAL

# Path to the log file
LOGGER_PATH = 'logs/'
LOGGER_FILE_SUFFIX = '.log'

LOG_FILE = f'{LOGGER_PATH}logger{LOGGER_FILE_SUFFIX}'

# Path to the data directory
DATA_DIR = 'data/'

# CONFIGURATION

# Configuration file name
CONFIG_FILE = 'config.json'

# Valid configuration keys
CONFIG_KEYS: Dict[str, Type] = {
    'DATA_DIR': str,
    
    'LOGGING': {
        'LEVEL': str,
        'LOG_FILE': str
    },

    'LOAD_GENES_AT_STARTUP': bool
    
}

# Logging levels
LOGGING_LEVELS = {
    'DEBUG': 0,
    'INFO': 1,
    'WARNING': 2,
    'ERROR': 3,
    'CRITICAL': 4
}