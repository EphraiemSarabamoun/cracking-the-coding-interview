import random

class RandomTreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1

class RandomBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(node):
            if not node:
                return RandomTreeNode(val)
            if val <= node.val:
                node.left = _insert(node.left)
            else:
                node.right = _insert(node.right)
            node.size += 1
            return node
        self.root = _insert(self.root)

    def get_random_node(self):
        if not self.root:
            return None
        def _get(node, index):
            left_size = node.left.size if node.left else 0
            if index == left_size:
                return node
            if index < left_size:
                return _get(node.left, index)
            return _get(node.right, index - left_size - 1)
        return _get(self.root, random.randint(0, self.root.size - 1))

if __name__ == "__main__":
    tree = RandomBinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    print(tree.get_random_node().val)
    
