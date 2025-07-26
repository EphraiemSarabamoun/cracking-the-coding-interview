class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None
        self.parent = None

def successor(node: TreeNode):
    if node.right:
        node = node.right
        while node.left:  # Find leftmost node in right subtree
            node = node.left
        return node
    else:
        while node.parent:
            if node.parent.left == node:
                return node.parent
            node = node.parent 
    return None



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    
    check_node = root.right
    print(successor(check_node).value if successor(check_node) else "No successor")