import unittest

from providers.data.DataProvider import DataProvider


class TestDataProvider(unittest.TestCase):
    def setUp(self):
        self.data_provider = DataProvider[str]()

    def test_add_data_stores_data_correctly(self):
        self.data_provider.add_data('test', 'test')
        self.assertEqual(self.data_provider.get_data('test'), 'test')

    def test_add_data_stores_data_correctly_with_nested_key(self):
        self.data_provider.add_data('test1/test2', 'test')
        self.assertEqual(self.data_provider.get_data('test1/test2'), 'test')

    def test_add_data_stores_data_correctly_with_multiple_nested_keys(self):
        self.data_provider.add_data('test1/test3', 'test')
        self.assertEqual(self.data_provider.get_data('test1/test3'), 'test')

    def test_add_data_overrides_existing_data(self):
        self.data_provider.add_data('test', 'test')
        self.data_provider.add_data('test', 'test1')
        self.assertEqual(self.data_provider.get_data('test'), 'test1')

    def test_add_data_raises_error_for_invalid_key(self):
        with self.assertRaises(ValueError) as context:
            self.data_provider.add_data('test/test2', 'test2')

    def test_get_data_returns_correct_data(self):
        self.data_provider.add_data('test', 'test')
        self.assertEqual(self.data_provider.get_data('test'), 'test')

    def test_get_data_returns_correct_data_with_nested_key(self):
        self.data_provider.add_data('test1/test2', 'test')
        self.assertEqual(self.data_provider.get_data('test1/test2'), 'test')

    def test_contains_returns_true_for_existing_key(self):
        self.data_provider.add_data('test', 'test')
        self.assertTrue('test' in self.data_provider)

    def test_contains_returns_false_for_nonexistent_key(self):
        self.assertFalse('nonexistent' in self.data_provider)

    def test_contains_returns_true_for_existing_nested_key(self):
        self.data_provider.add_data('test1/test2', 'test')
        self.assertTrue('test1' in self.data_provider)
