import pandas as pd
from typing import Dict, Union, TypeVar, Generic

from .DataTree import DataTree

T = TypeVar('T')

class DataProvider(Generic[T]):
    """
    The DataProvider class is a wrapper around the DataTree class that provides a more user-friendly interface.
    """

    data: DataTree[T] = DataTree[T]()

    def add_data(self, key: str, data: T):
        self.data.add_data(key, data)

    def get_data(self, key: str) -> Union[T, None]:
        return self.data.get_data(key)
    
    def remove_data(self, key: str):
        self.data.remove_data(key)

    def length(self) -> int:
        return self.data.length()
    
    def __str__(self):
        return str(self.data)
    
    