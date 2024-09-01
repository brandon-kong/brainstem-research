import unittest

from src.utils.DataTree import DataTree

class TestTree(unittest.TestCase):
    def test_tree_create(self):
        tree = DataTree()
        self.assertEqual(len(tree), 0)
        self.assertIsInstance(tree, DataTree)

    def test_tree_add_node(self):
        tree = DataTree()
        tree.add_node(['a', 'b', 'c'], 1)
        self.assertEqual(len(tree), 1)
        self.assertEqual(tree.get_node(['a', 'b', 'c']), 1)

    def test_tree_get_node(self):
        tree = DataTree()
        tree.add_node(['a', 'b', 'c'], 1)
        self.assertEqual(tree.get_node(['a', 'b', 'c']), 1)

    def test_tree_non_leaf_value(self):
        tree = DataTree()
        tree.add_node(['a', 'b', 'c'], 1)
        self.assertEqual(tree.get_node(['a', 'b']), None)

    def test_tree_length(self):
        tree = DataTree()
        tree.add_node(['a', 'b', 'c'], 1)
        tree.add_node(['a', 'b', 'd'], 2)
        self.assertEqual(len(tree), 2)