class Node:
    def __init__(self, val, next = None):
        self.val = val 
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        node = self.head.next
        while index > 0:
            node = node.next
            index -= 1
        print(node.val)
        return node.val
    
    def appendHead(self, val: int) -> None:
        newHead = Node(val)
        newHead.next = self.head.next
        self.head.next = newHead
        self.size += 1
    
    def appendTail(self, val: int) -> None:
        index = self.size
        last = self.head.next
        while index > 1:
            last = last.next
            index -= 1
        last.next = Node(val)
        self.size += 1
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        temp = Node(val)
        if index == 0 and self.size == 0:
            self.head.next = temp
            self.size += 1
            return
        elif index == 0 and self.size == 1:
            temp.next = self.head.next
            self.head.next = temp
            self.size += 1
            return
        node = self.head.next
        while index > 1:
            node = node.next
            index -= 1 
        temp.next = node.next
        node.next = temp
        self.size += 1
    
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0 and self.size <= 1:
            self.head.next = None
            self.size -= 1
            return
        elif index == 0:
            self.head.next = self.head.next.next
            self.size -= 1
        node = self.head.next
        while index > 1:
            node = node.next
            index -= 1 
        node.next = node.next.next
        self.size -= 1