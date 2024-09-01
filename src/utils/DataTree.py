from typing import TypeVar, Generic, List, Dict, Tuple, Any

T = TypeVar('T')

class Node(Generic[T]):
    """
    Node class

    This class is used to store data in a tree structure. It is used to store the data in a tree structure
    analagous to the directory structure in a file system.
    """
    def __init__(self, data: T):
        self.data = data
        self.children: Dict[str, Node[T]] = {}

    def add_child(self, key: str, data: T) -> None:
        """
        Add a child node to the current node

        Args:
            key (str): Key to access the child node
            data (any): Data to be stored in the child node
        """
        self.children[key] = Node(data)

    def get_child(self, key: str) -> T:
        """
        Get the data stored in a child node

        Args:
            key (str): Key to access the child node

        Returns:
            any: Data stored in the child node
        """
        return self.children[key].data

    def get_children(self) -> Dict[str, T]:
        """
        Get the data stored in all the child nodes

        Returns:
            dict: Dictionary where the keys are the keys of the child nodes and the values are the data stored in the child nodes
        """
        children = {}
        for key in self.children:
            children[key] = self.children[key].data
        return children

    def get_leaf_nodes(self) -> List[Tuple[str, T]]:
        """
        Get the leaf nodes of the tree

        Returns:
            list: List of tuples where the first element is the key of the node and the second element is the data stored in the node
        """
        nodes = []
        def get_nodes_recursive(node, key):
            for k in node:
                new_key = key + [k]
                if len(node[k].children) == 0:
                    nodes.append((new_key, node[k].data))
                else:
                    get_nodes_recursive(node[k].children, new_key)
        get_nodes_recursive(self.children, [])
        return nodes

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
                get_keys_recursive(node[k].children, new_key)
        get_keys_recursive(self.children, [])
        return keys
    
    def get_non_null_nodes(self) -> List[Tuple[List[str], T]]:
        """
        Get the non-null nodes of the tree

        Returns:
            list: List of tuples where the first element is the key of the node and the second element is the data stored in the node
        """
        nodes = []
        def get_nodes_recursive(node, key):
            for k in node:
                new_key = key + [k]
                if node[k].data is not None:
                    nodes.append((new_key, node[k].data))
                get_nodes_recursive(node[k].children, new_key)
        get_nodes_recursive(self.children, [])
        return nodes

class DataTree(Generic[T]):
    """
    DataTree class

    This class is used to store data in a tree structure. It is used to store the data in a tree structure
    analagous to the directory structure in a file system.
    """
    
    def __init__(self):
        self.root: Node[T] = Node(None)

    def add_node(self, key: List[str], data: T) -> None:
        """
        Add a node to the tree

        Args:
            key (list): List of keys to access the node
            data (any): Data to be stored in the node
        """
        node = self.root
        for k in key:
            if k not in node.children:
                node.add_child(k, None)
            node = node.children[k]
        node.data = data

    def get_node(self, key: List[str]) -> T:
        """
        Get the data stored in a node

        Args:
            key (list): List of keys to access the node

        Returns:
            any: Data stored in the node
        """
        node = self.root
        for k in key:
            if k not in node.children:
                return None
            node = node.children[k]
        return node.data

    def get_keys(self) -> List[List[str]]:
        """
        Get the keys of all the nodes in the tree

        Returns:
            list: List of keys of all the nodes in the tree
        """
        return self.root.get_keys()

    def get_leaf_nodes(self) -> List[Tuple[List[str], T]]:
        """
        Get the leaf nodes of the tree

        Returns:
            list: List of tuples where the first element is the key of the node and the second element is the data stored in the node
        """
        return self.root.get_leaf_nodes()
    
    def __len__(self) -> int:
        """
        Get the number of nodes in the tree
        Non-leaf nodes are not counted

        Returns:
            int: Number of nodes in the tree
        """
        return len(self.root.get_non_null_nodes())