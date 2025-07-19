class Node:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next

def sum_lists(head1, head2):
    current1 = head1
    current2 = head2
    dummyhead = Node(0)
    dummy = dummyhead
    carry = 0
    while current1 or current2:
        total = current1.val + current2.val + carry
        if total >= 10:
            carry = 1
            dummy.next = Node(total % 10)
        else:
            carry = 0
            dummy.next = Node(total)
        current1 = current1.next
        current2 = current2.next
        dummy = dummy.next
    if carry != 0:
        dummy.next = Node(carry)
    return dummyhead.next 
if __name__ == "__main__":
    print(sum_lists(Node(5, Node(4, Node(3, Node(4, Node(5))))),Node(5, Node(1, Node(3, Node(4, Node(5)))))).next.next.next.next.next.val)
