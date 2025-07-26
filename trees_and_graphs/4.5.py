class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def check_binary_search_tree(root: TreeNode):
    if root == None: 
        return True
    if root.left:
        if root.left.value > root.value:
            return False
        else:
            return check_binary_search_tree(root.left)
    if root.right:
        if root.right.value < root.value:
            return False
        else:
            return check_binary_search_tree(root.right)
    return True

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(1)
    
    print(check_binary_search_tree(root))