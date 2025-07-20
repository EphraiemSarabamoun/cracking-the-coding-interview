from collections import deque

class Animal_Shelter:
    def __init__(self):
        self.dog = deque()
        self.cat = deque()
        self.order = 0
    def enqueue(self,animal):
        self.order += 1
        if animal == "dog":
            self.dog.append((animal,self.order))
        else:
            self.cat.append((animal,self.order))
    def dequeue_any(self):
        if self.dog and self.cat:
            if self.dog[-1][1] < self.cat[-1][1]:
                return self.dog.pop()
            else:
                return self.cat.pop()
        elif self.dog:
            return self.dog.pop()
        elif self.cat:
            return self.cat.pop()
        else:
            return None
    def dequeue_dog(self):
        if not self.dog:
            return None
        return self.dog.pop()
    def dequeue_cat(self):
        if not self.cat:
            return None
        return self.cat.pop() 