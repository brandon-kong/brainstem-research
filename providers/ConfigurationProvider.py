from typing import Union, Dict, Final

from .data.DataProvider import DataProvider
from utils.constants import JSONable

from utils.Printer import Printer
from utils.logger.Logger import Logger

class ConfigurationProvider:
    """
    The ConfigurationProvider class is a singleton class that provides a way to store and retrieve configuration data.
    """
    
    printer: Printer = None
    logger: Logger = None

    data_provider: Final[DataProvider[JSONable]] = DataProvider[JSONable]()
    
    def __init__(self, printer: Printer, logger: Logger) -> None:
        self.printer = printer
        self.logger = logger

    def load_configuration(self, configuration: Dict[str, JSONable], valid_keys: Dict[str, type]):
        for key, data in configuration.items():
            if key in valid_keys:
                valid_type_or_dict = valid_keys[key]
                if isinstance(valid_type_or_dict, dict):
                    # If the valid "type" is actually a dictionary, we need to handle it separately
                    if isinstance(data, dict):
                        self.load_configuration(data, valid_type_or_dict)
                    else:
                        self.logger.error(f"Invalid type for key: {key}. Expected {valid_type_or_dict}, got {type(data)}")
                elif isinstance(data, valid_type_or_dict):
                    self.add_configuration(key, data)
                else:
                    self.logger.error(f"Invalid type for key: {key}. Expected {valid_type_or_dict}, got {type(data)}")
            else:
                self.logger.error(f'Invalid key: {key}')
    
    def add_configuration(self, key: str, data: JSONable):
        self.data_provider.add_data(key, data)
    
    def get_configuration(self, key: str) -> Union[JSONable, None]:
        return self.data_provider.get_data(key)

    def length(self) -> int:
        return self.data_provider.length()
    
    def __str__(self):
        return str(self.data_provider)
    
    def __repr__(self):
        return repr(self.data_provider)