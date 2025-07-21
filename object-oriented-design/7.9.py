class CircularArray:
    def __init__(self,size):
        self.array = [None]*size
        self.head = 0
    def get(self, index):
        return self.array[(index + self.head) % len(self.array)]
    def set(self, index, value):
        self.array[(index + self.head) % len(self.array)] = value
    def rotate(self):
        self.head = (self.head + 1) % len(self.array)
        return self.head


if __name__ == "__main__":
    circulararray = CircularArray(5)
    circulararray.set(0,1)
    circulararray.set(1,2)
    circulararray.set(2,3)
    circulararray.set(3,4)
    circulararray.set(4,5)
    print(circulararray.get(0))
    print(circulararray.get(1))
    print(circulararray.get(2))
    print(circulararray.get(3))
    print(circulararray.get(4))
    print("Now we rotate")
    circulararray.rotate()
    print(circulararray.get(0))
    print(circulararray.get(1))
    print(circulararray.get(2))
    print(circulararray.get(3))
    print(circulararray.get(4))