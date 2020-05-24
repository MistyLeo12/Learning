class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if not self.items:
            #print("The stack is empty")
            return True
        else:
           return False

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.isEmpty():
            return
        else:
            return self.items.pop()
    
    def peek(self): #Returns the top element on the stack
        if not self.isEmpty():
            return self.items[-1]
    
    def returnStack(self):
        return self.items
    