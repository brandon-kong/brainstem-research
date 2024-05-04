import unittest

from providers.data.DataProvider import DataProvider

class TestDataProvider(unittest.TestCase):
    def setUp(self):
        self.data_provider = DataProvider[str]()
        
    def test_add_data(self):
        self.data_provider.add_data('test', 'test')
        self.assertEqual(self.data_provider.get_data('test'), 'test')

        self.data_provider.add_data('test1/test2', 'test')
        self.assertEqual(self.data_provider.get_data('test1/test2'), 'test')

