from typing import Union, Dict, Final

from providers.data.DataProvider import DataProvider
from utils.constants import (
    JSONABLE
)

from utils.Printer import Printer

from exceptions.ConfigurationExceptions import (
    ConfigurationLoadException
)


class ConfigurationProvider:
    """
    The ConfigurationProvider class is a singleton class that provides a way to store and retrieve configuration data.
    """

    __instance = None
    data_provider: Final[DataProvider[JSONABLE]] = DataProvider[JSONABLE]()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ConfigurationProvider, cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        pass

    def _handle_nested_dict(self, key: str, data: JSONABLE, valid_type_or_dict: Dict[str, type]) -> None:
        if isinstance(data, dict):
            self.load_configuration(data, valid_type_or_dict)
        else:
            raise ConfigurationLoadException(f"Invalid type for key: {key}. Expected dict, got {type(data)}")

    def _validate_and_add(self, key: str, data: JSONABLE, expected_type: type) -> None:
        if isinstance(data, expected_type):
            self.add_configuration(key, data)
        else:
            raise ConfigurationLoadException(f"Invalid type for key: {key}. Expected {expected_type}, got {type(data)}")

    def load_configuration(self, configuration: Dict[str, JSONABLE],
                           valid_keys: Dict[str, Union[type, Dict[str, type]]]) -> None:
        for key, data in configuration.items():
            if key in valid_keys:
                valid_type_or_dict = valid_keys[key]
                if isinstance(valid_type_or_dict, dict):
                    self._handle_nested_dict(key, data, valid_type_or_dict)
                else:
                    self._validate_and_add(key, data, valid_type_or_dict)
            else:
                # Invalid key, this doesn't affect the program, so we just log it
                Printer.warning(f'[ConfigurationProvider] Invalid key: {key}')

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
