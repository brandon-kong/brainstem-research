from .data.DataProvider import DataProvider

from typing import Union, Dict, Final

type JSONable = Union[str, int, float, bool, None, Dict[str, JSONable]]

class ConfigurationProvider:
    """
    The ConfigurationProvider class is a singleton class that provides a way to store and retrieve configuration data.
    """
    
    __instance: 'ConfigurationProvider' = None
    data_provider: Final[DataProvider[JSONable]] = DataProvider[JSONable]()

    def __new__(cls) -> 'ConfigurationProvider':
        if cls.__instance is None:
            cls.__instance = super(ConfigurationProvider, cls).__new__(cls)
        
        return cls.__instance
    
    def __init__(self):
        pass

    def load_configuration(self, configuration: Dict[str, JSONable]):
        for key, data in configuration.items():
            self.add_configuration(key, data)
    
    def add_configuration(self, key: str, data: JSONable):
        self.data_provider.add_data(key, data)
    
    def get_configuration(self, key: str) -> Union[JSONable, None]:
        return self.data_provider.get_data(key)
    
    def remove_configuration(self, key: str):
        self.data_provider.remove_data(key)
    
    def __str__(self):
        return str(self.data_provider)
    
    def __repr__(self):
        return repr(self.data_provider)