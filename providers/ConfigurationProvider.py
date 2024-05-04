from typing import Union, Dict, Final

from .data.DataProvider import DataProvider
from utils.constants import JSONable

from utils.Printer import Printer
from utils.logger.Logger import Logger

class ConfigurationProvider:
    """
    The ConfigurationProvider class is a singleton class that provides a way to store and retrieve configuration data.
    """
    
    __instance: 'ConfigurationProvider' = None
    printer: Printer = None
    logger: Logger = None

    data_provider: Final[DataProvider[JSONable]] = DataProvider[JSONable]()

    def __new__(cls, printer: Printer, logger: Logger) -> 'ConfigurationProvider':
        if cls.__instance is None:
            cls.__instance = super(ConfigurationProvider, cls).__new__(cls)
            cls.__instance.printer = printer
            cls.__instance.logger = logger
        return cls.__instance
    
    def __init__(self, printer: Printer, logger: Logger) -> None:
        pass

    def load_configuration(self, configuration: Dict[str, JSONable], valid_keys: Dict[str, type]):
        for key, data in configuration.items():
            if key in valid_keys:
                if isinstance(data, valid_keys[key]):
                    self.add_configuration(key, data)
                else:
                    # Invalid type
                    self.printer.warning(f"Invalid type for key: {key}. Expected {valid_keys[key]}, got {type(data)}")
            else:
                # Invalid key
                self.printer.warning(f"Invalid key: {key}")
    
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