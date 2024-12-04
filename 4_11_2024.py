
class Stack:
    def __init__(self, max_size=None):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if self.max_size is not None and len(self.items) >= self.max_size:
            print(f"Error: Stack overflow, item '{item}' cannot be pushed")
        else:
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
stack = Stack(max_size=2)
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

