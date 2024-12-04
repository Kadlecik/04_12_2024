class Stack:
    def __init__(self, max_size=None):
        self.__items = []
        self.__max_size = max_size

    def push(self, item):
        if (self.__max_size is not None and len(self.__items) >= self.__max_size):
            print(f"Error: Stack overflow, item '{item}' cannot be pushed")
        else:
            self.__items.append(item)

    def pop(self):
        if not self.__isEmpty():
            return self.__items.pop()
        return None

    def top(self):
        if not self.__isEmpty():
            return self.__items[-1]
        return None

    def isEmpty(self):
        return len(self.__items) == 0

    def actual_size(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)

    def __isEmpty(self):
        pass


# Příklad použití:
stack = Stack(max_size=2)
stack.push(1)
stack.push(2)
stack.push(3)  # Výstup: Error: Stack overflow, item '3' cannot be pushed
print(stack)        # Výstup: [1, 2]
print(stack.top())  # Výstup: 2
stack.pop()
print(stack)        # Výstup: [1]
print(stack.isEmpty())  # Výstup: False
print(stack.actual_size())  # Výstup: 1
