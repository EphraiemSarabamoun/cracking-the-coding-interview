class BiNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def convert_to_list(root: BiNode) -> BiNode:
    def convert(node: BiNode) -> tuple[BiNode, BiNode]:  # Head, tail
        if not node:
            return None, None
        left_head, left_tail = convert(node.left)
        right_head, right_tail = convert(node.right)
        if left_tail:
            left_tail.right = node
        node.left = left_tail
        node.right = right_head
        head = left_head or node
        tail = right_tail or node
        return head, tail
    head, _ = convert(root)
    return head