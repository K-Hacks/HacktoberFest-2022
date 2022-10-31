import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size
        self.top=-1

    def is_empty(self):
        return self.top==-1

    def is_full(self):
        return self.top==self.size-1

    def push(self, data):
        if not self.is_full():
            self.top+=1
            self.items.append(values[1])

    def pop(self):
        if not self.is_empty():
            del self.items[self.top]
            self.top-=1
    def status(self):
        for i in self.items:
            print(i)
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
