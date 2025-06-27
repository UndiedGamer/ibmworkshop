class Queue():
    def __init__(self):
        self.items = []
        self.rear = -1
        self.back = -1

    def push(self, element):
        self.items.append(element)
        if self.rear == -1:
            self.rear = self.rear+1
        self.back = self.back+1
        print(f"Pushed {element} to stack")

    def pop(self):
        if self.rear>0:
            return self.items.pop(self.rear)
        else:
            raise Exception("Queue Underflow")
        
    def peek(self):
        return self.items[self.rear] if self.rear>0 else None