from typing import Union, Dict, Final

from .data.DataProvider import DataProvider
from utils.constants import JSONABLE

from utils.Printer import Printer


class ConfigurationProvider:
    """
    The ConfigurationProvider class is a singleton class that provides a way to store and retrieve configuration data.
    """

    data_provider: Final[DataProvider[JSONABLE]] = DataProvider[JSONABLE]()

    def __init__(self) -> None:
        pass

    def load_configuration(self, configuration: Dict[str, JSONABLE],
                           valid_keys: Dict[str, Union[type, Dict[str, type]]]) -> None:
        for key, data in configuration.items():
            if key in valid_keys:
                valid_type_or_dict = valid_keys[key]
                if isinstance(valid_type_or_dict, dict):
                    # If the valid "type" is actually a dictionary, we need to handle it separately
                    if isinstance(data, dict):
                        self.load_configuration(data, valid_type_or_dict)
                    else:
                        Printer.error(f"Invalid type for key: {key}. Expected {valid_type_or_dict}, got {type(data)}")
                elif isinstance(data, valid_type_or_dict):
                    self.add_configuration(key, data)
                else:
                    Printer.error(f"Invalid type for key: {key}. Expected {valid_type_or_dict}, got {type(data)}")
            else:
                Printer.error(f'Invalid key: {key}')

    def add_configuration(self, key: str, data: JSONABLE):
        self.data_provider.add_data(key, data)

    def get_configuration(self, key: str) -> Union[JSONABLE, None]:
        return self.data_provider.get_data(key)

    def length(self) -> int:
        return self.data_provider.length()

    def keys(self):
        return self.data_provider.keys()

    def __contains__(self, key: str) -> bool:
        return key in self.data_provider

    def __getitem__(self, key: str) -> JSONABLE:
        return self.get_configuration(key)

    def __str__(self):
        return str(self.data_provider)

    def __repr__(self):
        return repr(self.data_provider)
