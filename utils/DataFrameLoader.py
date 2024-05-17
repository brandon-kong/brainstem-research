import os
from typing import Dict

import dask.dataframe as dd


class DataFrameLoader:

    @staticmethod
    def load_dataframes_in_directory(directory: str) -> Dict[str, dd.DataFrame]:
        """
        Load all dataframes in a directory.
        :param directory: The directory to load the dataframes from.
        :return: A dictionary of dataframes.
        """
        dataframes = {}
        for file in os.listdir(directory):
            if file.endswith('.csv'):
                # get the name of the file without the extension
                name = os.path.splitext(file)[0]
                dataframes[name] = dd.read_csv(os.path.join(directory, file))

        return dataframes

    @staticmethod
    def load_dataframes_in_directory_with_keys(directory: str, keys: Dict[str, str]) -> Dict[str, dd.DataFrame]:
        """
        Load all dataframes in a directory with specific keys.
        :param directory: The directory to load the dataframes from.
        :param keys: The keys to use for the dataframes.
        :return: A dictionary of dataframes.
        """
        dataframes = {}
        for file, key in keys.items():
            if file.endswith('.csv'):
                name = os.path.splitext(file)[0]
                dataframes[name] = dd.read_csv(os.path.join(directory, file))

        return dataframes
