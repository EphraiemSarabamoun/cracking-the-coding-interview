class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self,size):
        self.table = [None]*size
        self.size = size
    def hash(self,key):
        return hash(key) % self.size
    def insert(self,key,value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key,value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key,value)
    def get(self,key):
        index = self.hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return

if __name__ == "__main__":
    hashtable = HashTable(2)
    hashtable.insert("a",1)
    hashtable.insert("b",2)
    hashtable.insert("c",3)
    print(hashtable.get("a"))
    print(hashtable.get("b"))
    print(hashtable.get("c"))