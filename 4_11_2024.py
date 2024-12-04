
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def isEmpty(self):
        return len(self.items) == 0

    def actual_size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Příklad použití:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print(stack.top())
stack.pop()
print(stack)
print(stack.isEmpty())
print(stack.actual_size())  