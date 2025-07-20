class SetOfStacks:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = [[]]
    def push(self,value):
        if len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(value)
        else:
            self.stacks.append([value])
    def pop(self):
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return self.stacks[-1].pop()
    def pop_at(self,index):
        if len(self.stacks) >= index:
            return None
        return self.stacks[index].pop()
        