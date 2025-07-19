class Node:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next

def partition(head,x):
    if head is None:
        return None
    current = head
    head1 = Node(0)
    head2 = Node(0)
    dummy1 = head1
    dummy2 = head2
    while current:
        if current.val < x:
            dummy1.next = current
            dummy1 = dummy1.next
        else:
            dummy2.next = current
            dummy2 = dummy2.next
        current = current.next
    dummy1.next = head2.next
    dummy2.next = None
    return head1.next

if __name__ == "__main__":
    print(partition(Node(5, Node(2, Node(3, Node(4, Node(5))))), 3).val)
    
