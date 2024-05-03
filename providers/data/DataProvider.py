import pandas as pd
from typing import Dict, Union

from .DataTree import DataTree

# Type definition for the data node
DataNode = Dict[str, Union[pd.DataFrame, 'DataNode']]


class DataProvider(object):
    """
    The DataProvider class is a singleton that abstracts the DataTree class.
    """

    __instance: Union['DataProvider', None] = None
    data: DataTree = DataTree()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DataProvider, cls).__new__(cls)
        return cls.__instance

    def add_data(self, key: str, df: pd.DataFrame):
        self.data.add_data(key, df)

    def get_data(self, key: str) -> Union[pd.DataFrame, None]:
        return self.data.get_data(key)
    
    def save_data_to_file(self, key: str, file_path: str):
        df = self.get_data(key)
        if df is not None:
            df.to_csv(file_path)
    
    def __str__(self):
        return str(self.data)