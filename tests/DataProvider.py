import unittest

from providers.data.DataProvider import DataProvider

class TestDataProvider(unittest.TestCase):
    def setUp(self):
        self.data_provider = DataProvider()

    def test_add_data(self):
        self.data_provider.add_data('test', 'test')
        self.assertEqual(self.data_provider.get_data('test'), 'test')

    def test_save_data_to_file(self):
        self.data_provider.add_data('test', 'test')
        self.data_provider.save_data_to_file('test', 'test.csv')

if __name__ == '__main__':
    unittest.main()