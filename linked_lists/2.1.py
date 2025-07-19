class Node:
    def __init__(self,val: int,next=None):
        self.val = val
        self.next = next

def remove_duplicates(head: Node) -> Node:
    if head is None:
        return None
    current = head
    my_set = {current.val}
    while current.next:
        if current.next.val in my_set:
            current.next = current.next.next
        else:
            my_set.add(current.next.val)
            current = current.next
    return head


if __name__ == "__main__":
    print(remove_duplicates(Node(1, Node(1, Node(1, Node(4, Node(5)))))).next.val)