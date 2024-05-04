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

    def print(self, message):
        print(message)

    def error(self, message):
        print(f'\033[91mError: {message}\033[0m')

    def warning(self, message):
        print(f'\033[93mWarning: {message}\033[0m')

    def success(self, message):
        print(f'\033[92m{message}\033[0m')

    def info(self, message):
        print(f'\033[94m{message}\033[0m')