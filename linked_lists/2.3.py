class Node:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next
def delete_middle_node(node: Node) -> None:
    if node is None or node.next is None:
        return None
    node.val = node.next.val
    node.next = node.next.next
    return node
if __name__ == "__main__":
    print(delete_middle_node(Node(1, Node(2, Node(3, Node(4, Node(5)))))).next.val)