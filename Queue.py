class Queue:
    def __init__(self):
        self.items = []

    def addLast(self, item):
        self.items.append(item)

    def deleteFirst(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def getFirst(self):
        if not self.isEmpty():
            return self.items[0]
        return None

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Příklad použití:
queue = Queue()
queue.addLast(1)
queue.addLast(2)
print(queue)         # Výstup: [1, 2]
print(queue.getFirst())  # Výstup: 1
queue.deleteFirst()
print(queue)         # Výstup: [2]
print(queue.isEmpty())   # Výstup: False
print(queue.size())      # Výstup: 1
