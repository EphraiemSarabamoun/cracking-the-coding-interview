class Node:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next
def return_kth_to_last(head: Node,k: int) -> Node:
    if head is None:
        return None
    current = head
    count = 0
    while current:
        count += 1
        if count == k:
            return current
        current = current.next
    return None

if __name__ == "__main__":
    print(return_kth_to_last(Node(1, Node(2, Node(3, Node(4, Node(5))))), 3).val)
