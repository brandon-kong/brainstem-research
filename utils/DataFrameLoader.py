import os
from typing import Dict

import dask.dataframe as dd


class DataFrameLoader:

    @staticmethod
    def load_dataframes_in_directory(directory: str) -> Dict[str, dd.DataFrame]:
        """
        Load all dataframes in a directory, including those in subdirectories.
        :param directory: The directory to load the dataframes from.
        :return: A dictionary of dataframes.
        """
        dataframes = {}
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.csv'):
                    path = os.path.join(root, file)
                    name = os.path.splitext(os.path.relpath(path, directory))[0]
                    dataframes[name] = dd.read_csv(path)

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
