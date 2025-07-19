class Node:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next

def intersection(head1, head2):
    current1 = head1
    current2 = head2
    while current1.next:
        current1 = current1.next
    while current2.next:
        current2 = current2.next
    if current1 == current2:
        return True
    return False    
 
if __name__ == "__main__":
    node = Node(7)
    print(intersection(Node(5, Node(4, Node(3, Node(4, Node(5,node))))),Node(5, Node(1, Node(3, Node(4, Node(5,node)))))))
    
