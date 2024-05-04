import os

class FileUtility:
    @staticmethod
    def create_directory(path):
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

    @staticmethod
    def create_file(path):
        if not os.path.exists(path):
            FileUtility.create_directory(path)
            with open(path, 'w') as f:
                f.write('')