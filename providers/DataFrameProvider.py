from typing import Union, Dict, Final

import dask.dataframe as dd
from .data.DataProvider import DataProvider


class DataFrameProvider:
    """
    The DataFrameProvider class is a singleton class that provides a way to store and retrieve dataframes from pandas.
    """

    __instance = None
    data_provider: Final[DataProvider[dd.DataFrame]] = DataProvider[dd.DataFrame]()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DataFrameProvider, cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        pass

    def load_dataframes(self, dataframes: Dict[str, dd.DataFrame]) -> None:
        for key, dataframe in dataframes.items():
            self.add_dataframe(key, dataframe)

    def add_dataframe(self, key: str, dataframe: dd.DataFrame):
        self.data_provider.add_data(key, dataframe)

    def get_dataframe(self, key: str) -> Union[dd.DataFrame, None]:
        return self.data_provider.get_data(key)

    def length(self) -> int:
        return self.data_provider.length()

    def keys(self):
        return self.data_provider.keys()

    def __contains__(self, key: str) -> bool:
        return key in self.data_provider

    def __getitem__(self, key: str) -> dd.DataFrame:
        return self.get_dataframe(key)

    def __str__(self):
        return str(self.data_provider)

    def __repr__(self):
        return repr(self.data_provider)
