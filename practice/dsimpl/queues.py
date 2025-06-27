class Queue():
    def __init__(self):
        self.items = []
        self.front = -1
        self.rear = -1

    def push(self, element):
        self.items.append(element)
        if self.front == -1:
            self.front = self.front+1
        self.rear = self.rear+1
        print(f"Pushed {element} to stack")

    def pop(self):
        if self.front>0:
            return self.items.pop(self.front)
        else:
            raise Exception("Queue Underflow")
        
    def peek(self):
        return self.items[self.front] if self.front>0 else None