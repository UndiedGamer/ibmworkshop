class Stack():
    def __init__(self):
        self.items = []
        self.top = 0

    def push(self, element):
        self.items.append(element)
        self.top = self.top+1
        print(f"Pushed {element} to stack")

    def pop(self):
        if self.top>0:
            self.top = self.top-1
            return self.items.pop()
        else:
            raise Exception("Stack Underflow")
        
    def peek(self):
        return self.items[self.top] if self.top>0 else None