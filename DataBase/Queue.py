class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print('added')

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0

    def fix_empty_issue(self):
        if self.is_empty():
            self.enqueue("default")
