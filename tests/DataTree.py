import unittest

from providers.data.DataTree import DataTree

class TestDataTree(unittest.TestCase):
    def setUp(self):
        self.data_tree = DataTree()

    def test_add_data(self):
        self.data_tree.add_data('test', 'test')
        self.assertEqual(self.data_tree.get_data('test'), 'test')

        self.data_tree.add_data('test1/test2', 'test')
        self.assertEqual(self.data_tree.get_data('test1/test2'), 'test')

    def test_add_data_override(self):
        self.data_tree.add_data('test', 'test')
        self.assertEqual(self.data_tree.get_data('test'), 'test')

        self.data_tree.add_data('test', 'test1')
        self.assertEqual(self.data_tree.get_data('test'), 'test1')

    def test_get_data(self):
        self.data_tree.add_data('test', 'test')
        self.assertEqual(self.data_tree.get_data('test'), 'test')

        self.data_tree.add_data('test1/test2', 'test')
        self.assertEqual(self.data_tree.get_data('test1/test2'), 'test')

        self.assertIsNone(self.data_tree.get_data('test1/test3'))
        self.assertIsNone(self.data_tree.get_data('test'))

    def test_get_data_empty_subtree(self):
        self.data_tree.add_data('test', 'test')
        self.assertIsNone(self.data_tree.get_data('test/test1'))

    def benchmark_add_data(self):
        for i in range(100000):
            self.data_tree.add_data(f'test{i}', 'test')
        
    def benchmark_get_data(self):
        for i in range(100000):
            self.data_tree.get_data(f'test{i}')
