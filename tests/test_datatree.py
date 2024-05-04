import unittest

from providers.data.DataTree import DataTree

class TestDataTree(unittest.TestCase):
    def setUp(self):
        self.data_tree = DataTree[str]()

    def test_add_data_stores_data_correctly(self):
        self.data_tree.add_data('test', 'test1')
        self.assertEqual(self.data_tree.get_data('test'), 'test1')

    def test_add_data_raises_error_for_invalid_key(self):
        self.data_tree.add_data('test/test1/test2', 'test3')

        self.assertRaises(ValueError, self.data_tree.add_data, 'test/test1', 'test4')

    def test_get_data_returns_correct_data(self):
        self.data_tree.add_data('test', 'test')
        self.assertEqual(self.data_tree.get_data('test'), 'test')

    def test_get_data_returns_none_for_nonexistent_key(self):
        self.assertIsNone(self.data_tree.get_data('test1/test3'))

    def test_get_data_empty_subtree_returns_none(self):
        self.data_tree.add_data('test', 'test')
        self.assertIsNone(self.data_tree.get_data('test/test1'))

    def test_length_returns_correct_length(self):
        test_tree = DataTree[str]()
        self.assertEqual(test_tree.length(), 0)
        test_tree.add_data('key1/key2', 'data')
        self.assertEqual(test_tree.length(), 1)
        test_tree.add_data('test/test2/test3', 'test')
        self.assertEqual(test_tree.length(), 2)

    def test_add_data_with_empty_key_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.data_tree.add_data('', 'test')
        self.assertEqual(str(context.exception), 'Key cannot be empty')

    def test_add_data_overwrites_existing_data(self):
        self.data_tree.add_data('test', 'test1')
        self.data_tree.add_data('test', 'test2')
        self.assertEqual(self.data_tree.get_data('test'), 'test2')

    def test_add_and_retrieve_none_value(self):
        self.data_tree.add_data('test', None)
        self.assertIsNone(self.data_tree.get_data('test'))

    def test_add_and_retrieve_empty_string(self):
        self.data_tree.add_data('test', '')
        self.assertEqual(self.data_tree.get_data('test'), '')

    def test_performance_with_large_data(self):
        for i in range(1000000):
            self.data_tree.add_data(str(i), 'test')
        self.assertEqual(self.data_tree.get_data('999999'), 'test')

    def test_add_and_retrieve_data_with_complex_nested_keys(self):
        self.data_tree.add_data('key1/key2/key3', 'test')
        self.assertEqual(self.data_tree.get_data('key1/key2/key3'), 'test')