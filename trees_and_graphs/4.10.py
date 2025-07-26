class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_subtree(t1: TreeNode, t2: TreeNode) -> bool:
    if not t2:
        return True
    if not t1:
        return False
    if match_trees(t1, t2):
        return True
    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)

def match_trees(n1, n2):
    if not n1 and not n2:
        return True
    if not n1 or not n2 or n1.val != n2.val:
        return False
    return match_trees(n1.left, n2.left) and match_trees(n1.right, n2.right)

if __name__ == "__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.left = TreeNode(4)
    t1.left.right = TreeNode(5)
    t1.right.left = TreeNode(6)
    t1.right.right = TreeNode(7)
    t1.left.left.left = TreeNode(8)
    
    t2 = TreeNode(2)
    t2.left = TreeNode(4)
    t2.right = TreeNode(5)
    
    print(is_subtree(t1, t2))