class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bst_sequences(root: TreeNode) -> list[list[int]]:
    def weave_lists(left, right, results, prefix):
        if not left or not right:
            result = prefix + left + right
            results.append(result)
            return
        weave_lists(left[1:], right, results, prefix + [left[0]])
        weave_lists(left, right[1:], results, prefix + [right[0]])

    def get_sequences(node):
        if not node:
            return [[]]
        left_seqs = get_sequences(node.left)
        right_seqs = get_sequences(node.right)
        sequences = []
        for left in left_seqs:
            for right in right_seqs:
                weaved = []
                weave_lists(left, right, weaved, [node.val])
                sequences.extend(weaved)
        return sequences

    return get_sequences(root)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    
    print(bst_sequences(root))