class TreeNode: 
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def height(node):
    if not node:
        return 0
    right_height = height(node.right)
    if right_height == -1:
        return -1
    left_height = height(node.left)
    if left_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return 1 + max(left_height, right_height)
def tree_balancing(root: TreeNode):
    if not root:
        return True
    return height(root) != -1

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    
    print(tree_balancing(root))