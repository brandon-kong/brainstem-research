"""
DataTree class

This class is used to store data in a tree structure. It is used to store the data in a tree structure
analagous to the directory structure in a file system. The tree is stored as a dictionary where the keys
are the names of the nodes and the values are the data stored in the nodes. 

The data can be of any type and the tree can be of any depth. The tree can be traversed using the get_node method which takes a list
of keys as input and returns the data stored in the node at the end of the list of keys. The tree can also
"""

class DataTree:
    def __init__(self):
        self.tree = {}

    def add_node(self, keys, data):
        """
        Add a node to the tree

        Args:
            keys (list): List of keys to traverse the tree to the node where the data is to be stored
            data (any): Data to be stored in the node
        """
        node = self.tree
        for key in keys[:-1]:
            if key not in node:
                node[key] = {}
            node = node[key]
        node[keys[-1]] = data

    def get_node(self, keys):
        """
        Get the data stored in a node

        Args:
            keys (list): List of keys to traverse the tree to the node where the data is stored

        Returns:
            any: Data stored in the node
        """
        node = self.tree
        for key in keys:
            if key not in node:
                return None
            node = node[key]
        return node

    def get_tree(self):
        """
        Get the entire tree

        Returns:
            dict: The tree
        """
        return self.tree

    def set_tree(self, tree):
        """
        Set the entire tree

        Args:
            tree (dict): The tree
        """
        self.tree = tree

    def get_keys(self):
        """
        Get the keys of all the nodes in the tree

        Returns:
            list: List of keys of all the nodes in the tree
        """
        keys = []
        def get_keys_recursive(node, key):
            for k in node:
                new_key = key + [k]
                keys.append(new_key)
                get_keys_recursive(node[k], new_key)
        get_keys_recursive(self.tree, [])
        return keys

    def get_nodes(self):
        """
        Get the data stored in all the nodes in the tree

        Returns:
            list: List of data stored in all the nodes in the tree
        """
        nodes = []
        def get_nodes_recursive(node):
            for k in node:
                if isinstance(node[k], dict):
                    get_nodes_recursive(node[k])
                else:
                    nodes.append(node[k])
        get_nodes_recursive(self.tree)
        return nodes

    def get_nodes_and_keys(self):
        """
        Get the data stored in all the nodes in the tree and the keys of the nodes

        Returns:
            list: List of tuples where the first element is the key of the node and the second element is the data stored in the node
        """
        nodes = []
        def get_nodes_recursive(node, key):
            for k in node:
                new_key = key + [k]
                if isinstance(node[k], dict):
                    get_nodes_recursive(node[k], new_key)
                else:
                    nodes.append((new_key, node[k]))
        get_nodes_recursive(self.tree, [])
        return nodes
    
    def get_nodes_and_keys_with_prefix(self, prefix):
        """
        Get the data stored in all the nodes in the tree and the keys of the nodes with a given prefix

        Args:
            prefix (list): The prefix to filter the keys

        Returns:
            list: List of tuples where the first element is the key of the node and the second element is the data stored in the node
        """
        nodes = []
        def get_nodes_recursive(node, key):
            for k in node:
                new_key = key + [k]
                if new_key[:len(prefix)] == prefix:
                    if isinstance(node[k], dict):
                        get_nodes_recursive(node[k], new_key)
                    else:
                        nodes.append((new_key, node[k]))
        get_nodes_recursive(self.tree, [])
        return nodes
    
    def get_nodes_with_prefix(self, prefix):
        """
        Get the data stored in all the nodes in the tree with a given prefix

        Args:
            prefix (list): The prefix to filter the keys

        Returns:
            list: List of data stored in the nodes
        """
        nodes = []
        def get_nodes_recursive(node, key):
            for k in node:
                new_key = key + [k]
                if new_key[:len(prefix)] == prefix:
                    if isinstance(node[k], dict):
                        get_nodes_recursive(node[k], new_key)
                    else:
                        nodes.append(node[k])
        get_nodes_recursive(self.tree, [])
        return nodes