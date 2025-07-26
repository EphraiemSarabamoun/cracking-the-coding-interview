from collections import deque

class TreeNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

class Node:
    def __init__ (self, value): 
        self.value = value
        self.next = None

def linked_list_depths(root: TreeNode): 
    if not root:
        return []
    levels = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)

        if queue[0].left:
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)

        level_head = Node(queue.popleft().value)
        current = level_head

        for _ in range(level_size - 1):
            tree_node = queue.popleft()
            
            new_node = Node(tree_node.value)
            

            current.next = new_node
            current = new_node
            
            if tree_node.left:
                queue.append(tree_node.left)
            if tree_node.right:
                queue.append(tree_node.right)
        
        levels.append(level_head)
    
    return levels

if __name__ == "__main__":
    
    # Example usage
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    result = linked_list_depths(root)
    
    for level in result:
        print(level.value)
        
    
