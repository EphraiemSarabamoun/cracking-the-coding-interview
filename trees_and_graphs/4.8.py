class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

def common_ancestor(root,q,p):
    if root == None or root == q or root == p:
        return root
    left = common_ancestor(root.left,q,p)
    right = common_ancestor(root.right,q,p)
    if left and right: 
        return root
    return left or right