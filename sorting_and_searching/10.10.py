class RankNode:
    def __init__(self, val: int):
        self.val = val
        self.left_size = 0
        self.left = None
        self.right = None

class RankStream:
    def __init__(self):
        self.root = None

    def insert(self, val: int):
        if not self.root:
            self.root = RankNode(val)
            return
        node = self.root
        while node:
            if val <= node.val:
                node.left_size += 1
                if not node.left:
                    node.left = RankNode(val)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = RankNode(val)
                    return
                node = node.right

    def get_rank(self, val: int) -> int:
        rank = 0
        node = self.root
        while node:
            if val == node.val:
                return rank + node.left_size
            elif val < node.val:
                node = node.left
            else:
                rank += node.left_size + 1
                node = node.right
        return -1