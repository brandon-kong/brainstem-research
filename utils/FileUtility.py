import os
import json

class FileUtility:

    @staticmethod
    def create_directory(path: str):
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

    @staticmethod
    def create_file(path: str):
        if not os.path.exists(path):
            FileUtility.create_directory(path)
            with open(path, 'w') as f:
                f.write('')

    @staticmethod
    def read_file(path: str):
        with open(path, 'r') as f:
            return f.read()
    
    @staticmethod
    def read_json(path: str):
        if not os.path.exists(path):
            return None
        return json.loads(FileUtility.read_file(path))