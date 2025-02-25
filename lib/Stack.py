class Stack:

    def __init__(self, items=[], limit=100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            print("Stack is full. Cannot push more items.")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        if not self.isEmpty():
            for i in range(len(self.items) - 1, -1, -1):
                if self.items[i] == target:
                    return len(self.items) - i - 1
        return -1
