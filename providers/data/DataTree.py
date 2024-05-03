import pandas as pd
from typing import Dict, Union

# Type definition for the data node
DataNode = Dict[str, Union[pd.DataFrame, 'DataNode', None]]


class DataTree:
    """
    The DataTree class is data structure that stores dataframes in a tree-like structure.
    """

    data: DataNode = {}

    def __init__(self):
        self.data = {}

    def add_data(self, key: str, df: pd.DataFrame):
        keys = key.split('/')
        last_key = keys.pop()
        current_dict: DataNode = self.data

        for key in keys:
            current_dict = current_dict.setdefault(key, {})

        current_dict[last_key] = df

    def get_data(self, key: str) -> Union[pd.DataFrame, None]:
        keys = key.split('/')
        current_dict: DataNode = self.data

        for key in keys:
            current_dict = current_dict.get(key, {})

        return current_dict if isinstance(current_dict, pd.DataFrame) else None
    
    def __str__(self):
        return str(self.data)