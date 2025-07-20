class Node: 
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
def minimal_tree(array: list) -> Node:
    def build(start,end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = Node(array[mid])
        node.left = build(start,mid-1)
        node.right = build(mid+1,end)
        return node
    return build(0,len(array)-1)
    
if __name__ == "__main__":
    print(minimal_tree([1,2,3,4,5,6,7]))