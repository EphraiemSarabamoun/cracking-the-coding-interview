class MyQueue:
    def __init__(self):
        self.stack_first = []
        self.stack_last = []
    def push(self,value):
        self.stack_first.append(value)
    def pop(self):
        if not self.stack_last:
            while self.stack_first:
                self.stack_last.append(self.stack_first.pop())
        return self.stack_last.pop()