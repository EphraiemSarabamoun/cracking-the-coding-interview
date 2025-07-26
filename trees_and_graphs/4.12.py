from collections import defaultdict

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def paths_with_sum(root: TreeNode, target: int) -> int:
    def dfs(node, running_sum, count):
        if not node:
            return 0
        running_sum += node.value
        paths = count[running_sum - target]
        count[running_sum] += 1
        paths += dfs(node.left, running_sum, count)
        paths += dfs(node.right, running_sum, count)
        count[running_sum] -= 1
        return paths

    count = defaultdict(int)
    count[0] = 1  
    return dfs(root, 0, count)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    
    print(paths_with_sum(root, 10))