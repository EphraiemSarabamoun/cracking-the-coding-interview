class Node:
    def __init__(self, val,next=None):
        self.val = val
        self.next = next

def loop_detection(head):
    current = head
    nodes = set()
    while current:
        if current in nodes:
            return current
        nodes.add(current)
        current = current.next
    return None
if __name__ == "__main__":
    print(loop_detection(Node(5, Node(4, Node(3, Node(4, Node(5)))))))
    print(loop_detection(Node(5, Node(1, Node(3, Node(4, Node(5)))))))
    print(loop_detection(Node(5, Node(4, Node(4, Node(5))))))
    
