class Printer:

    @staticmethod
    def print(message: str):
        print(message)

    @staticmethod
    def error(message: str):
        print(f'\033[91m{message}\033[0m')

    @staticmethod
    def warning(message: str):
        print(f'\033[93mWarning: {message}\033[0m')

    @staticmethod
    def success(message: str):
        print(f'\033[92m{message}\033[0m')

    @staticmethod
    def info(message: str):
        print(f'\033[94m{message}\033[0m')

    @staticmethod
    def debug(message: str):
        print(f'\033[95m{message}\033[0m')

    @staticmethod
    def loading(message: str):
        print(f'\033[96m{message}\033[0m')

    @staticmethod
    def custom(message: str, color: str):
        print(f'\033[{color}m{message}\033[0m')


class Color:
    CYAN = '96'
    MAGENTA = '95'
    YELLOW = '93'
    GREEN = '92'
    RED = '91'
