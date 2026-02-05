class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        elif self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            print("Stack is empty")
            return None
        return self.stack.pop()


class jadid(Queue, Stack):
    def __init__(self, size):
        super().__init__(size)
        Stack.__init__(self)

    def show_status(self):
        print("Queue:", self.queue)
        print("Stack:", self.stack)

obj = jadid(size=5)

obj.enqueue("A")
obj.enqueue("B")
obj.enqueue("C")

obj.push(1)
obj.push(2)
obj.push(3)

obj.show_status()

print("Dequeued:", obj.dequeue())
print("Popped:", obj.pop())
print("Popped:", obj.pop())

obj.show_status()