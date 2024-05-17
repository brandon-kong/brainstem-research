from typing import Dict, Union, Generic, TypeVar

# Type definition for the data node
T = TypeVar('T')


class DataNode(Dict[str, Union[T, 'DataNode', None]]):
    pass


class DataTree(Generic[T]):
    """
    The DataTree class is data structure that stores data in a tree-like structure.
    """

    data: DataNode = {}

    def __init__(self):
        self.data = DataNode()

    def add_data(self, key: str, data: T | Dict[str, Union[T, 'DataNode']]):
        if not key:
            raise ValueError('Key cannot be empty')

        keys = key.split('/')
        current_dict: DataNode = self.data

        for key in keys[:-1]:
            if key not in current_dict:
                current_dict[key] = {}

            # Check if the key is a value
            if not isinstance(current_dict[key], dict):
                raise ValueError(f'Key {key} is already a value')

            current_dict = current_dict[key]

        if keys[-1] in current_dict and isinstance(current_dict[keys[-1]], dict):
            raise ValueError(f'Key {keys[-1]} is already a dictionary')

        current_dict[keys[-1]] = data

    def get_data(self, key: str) -> Union[T, None]:
        if not key:
            return None

        keys = key.split('/')
        current_dict: DataNode = self.data

        for key in keys:
            if key not in current_dict:
                return

            current_dict = current_dict.get(key, None)

        return current_dict

    def remove_data(self, key: str):
        if not key:
            raise ValueError('Key cannot be empty')

        keys = key.split('/')
        current_dict: DataNode = self.data

        for key in keys[:-1]:
            if key not in current_dict:
                return

            current_dict = current_dict.get(key, None)

        if keys[-1] in current_dict:
            del current_dict[keys[-1]]

    def length(self) -> int:
        return self.length_recursive(self.data)

    def length_recursive(self, data: DataNode) -> int:
        count = 0
        for key in data:
            if isinstance(data[key], dict):
                count += self.length_recursive(data[key])
            else:
                count += 1
        return count

    def keys(self):
        return self.data.keys()

    def __str__(self):
        return str(self.data)

    def __contains__(self, key: str) -> bool:
        return key in self.keys()

    def __getitem__(self, key: str) -> T:
        return self.get_data(key)

    def __setitem__(self, key: str, data: T | Dict[str, Union[T, 'DataNode']]):
        self.add_data(key, data)
