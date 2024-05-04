class Printer:
    """
    Singleton class to print messages with colors
    """

    __instance: 'Printer' = None

    def __new__(cls) -> 'Printer':
        if cls.__instance is None:
            cls.__instance = super(Printer, cls).__new__(cls)
        
        return cls.__instance
    
    def __init__(self):
        pass

    def print(self, message: str):
        print(message)

    def error(self, message: str):
        print(f'\033[91mError: {message}\033[0m')

    def warning(self, message: str):
        print(f'\033[93mWarning: {message}\033[0m')

    def success(self, message: str):
        print(f'\033[92m{message}\033[0m')

    def info(self, message: str):
        print(f'\033[94m{message}\033[0m')

    def debug(self, message: str):
        print(f'\033[95m{message}\033[0m')

    def loading(self, message: str):
        print(f'\033[96m{message}\033[0m')

    def custom(self, message: str, color: str):
        print(f'\033[{color}m{message}\033[0m')

class Color:
    CYAN = '96'
    MAGENTA = '95'
    YELLOW = '93'
    GREEN = '92'