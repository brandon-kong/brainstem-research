import unittest

from providers.data.DataTree import DataTree

class TestDataTree(unittest.TestCase):
    def setUp(self):
        self.data_tree = DataTree[str]()

    def test_add_data(self):
        self.data_tree.add_data('test', "test")
        self.assertEqual(self.data_tree.get_data('test'), 'test')

        self.data_tree.add_data('test1/test2', 'test')
        self.assertEqual(self.data_tree.get_data('test1/test2'), 'test')

    def test_add_data_invalid_key(self):
        self.assertRaises(ValueError, self.data_tree.add_data, '', 'test')

    def test_add_data_override(self):
        self.data_tree.add_data('test', 'test')
        self.assertEqual(self.data_tree.get_data('test'), 'test')

        self.data_tree.add_data('test', 'test1')
        self.assertEqual(self.data_tree.get_data('test'), 'test1')

        self.assertRaises(ValueError, self.data_tree.add_data, 'test/test2', 'test2')

    def test_get_data(self):
        self.data_tree.add_data('test', 'test')
        self.assertEqual(self.data_tree.get_data('test'), 'test')

        self.data_tree.add_data('test1/test2', 'test')
        self.assertEqual(self.data_tree.get_data('test1/test2'), 'test')

        self.assertIsNone(self.data_tree.get_data('test1/test3'))
        self.assertIsNone(self.data_tree.get_data('test2'))

    def test_get_data_empty_subtree(self):
        self.data_tree.add_data('test', 'test')
        self.assertIsNone(self.data_tree.get_data('test/test1'))

    def test_length(self):
        test_tree = DataTree[str]()

        self.assertEqual(test_tree.length(), 0)

        test_tree.add_data('key1', {})
        self.assertEqual(test_tree.length(), 0)

        # Override the previous data
        test_tree.add_data('key1/key2', 'data')
        self.assertEqual(test_tree.length(), 1)

        test_tree.add_data('test/test2/test3', 'test')
        self.assertEqual(test_tree.length(), 2)

        test_tree.add_data('test4', 'test')
        self.assertEqual(test_tree.length(), 3)

    def test_remove_data(self):
        self.data_tree.add_data('test', 'test')
        self.assertEqual(self.data_tree.get_data('test'), 'test')

        self.data_tree.remove_data('test')
        self.assertIsNone(self.data_tree.get_data('test'))

    def test_remove_data_invalid_key(self):
        self.assertRaises(ValueError, self.data_tree.remove_data, '')

    def benchmark_add_data(self):
        for i in range(100000):
            self.data_tree.add_data(f'test{i}', 'test')
        
    def benchmark_get_data(self):
        for i in range(100000):
            self.data_tree.get_data(f'test{i}')
