import pandas as pd
from typing import Dict, Union, TypeVar, Generic

from .DataTree import DataTree

T = TypeVar('T')

class DataProvider(Generic[T]):
    """
    The DataProvider class is a singleton that abstracts the DataTree class.
    """

    __instance: Union['DataProvider[T]', None] = None
    data: DataTree[T] = DataTree[T]()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DataProvider, cls).__new__(cls)
        return cls.__instance

    def add_data(self, key: str, data: T):
        self.data.add_data(key, data)

    def get_data(self, key: str) -> Union[T, None]:
        return self.data.get_data(key)
    
    def __str__(self):
        return str(self.data)