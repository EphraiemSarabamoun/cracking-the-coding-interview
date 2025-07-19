class Node:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next

def palindrome(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    reversed_values = values[::-1]
    if values == reversed_values:
        return True
    return False    
if __name__ == "__main__":
    print(palindrome(Node(5, Node(4, Node(3, Node(4, Node(5)))))))
    print(palindrome(Node(5, Node(1, Node(3, Node(4, Node(5)))))))

    
