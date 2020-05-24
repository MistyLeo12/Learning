class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if not self.items:
            print("The queue is empty")
            return True
        else:
            return False
    
    def add(self, item):
        self.items.append(item)

    def remove(self):
        if self.isEmpty():
            return 
        else:
            return self.items.pop(0)
    
    def peek(self): #Returns the first element on the queue
        if not self.isEmpty():
            return self.items[1]
    
    def returnQueue(self):
        return self.items 
