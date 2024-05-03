class DataProvider(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(DataProvider, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)