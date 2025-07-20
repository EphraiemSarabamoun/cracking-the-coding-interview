class Stack:
    def __init__(self):
        self.array = []
        self.min = []
    def push(self,value):
        if not self.min or value < self.min[-1]:
            self.min.append(value)
        self.array.append(value)
        return
    def pop(self):
        if self.array[-1] == self.min[-1]:
            self.min.pop()
        return self.array.pop()
    def min(self):
        return self.min[-1]