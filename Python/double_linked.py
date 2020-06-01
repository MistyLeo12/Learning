
class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList(object):
    def __init__(self):
        self.root = Node()
        self.size = 0
    
    def get_size(self):
        current = self.root
        counter = 0
        while current.next is not None:
            counter += 1
            current = current.next
        return counter
    
    def push(self, data): #Inserts at head of the list 
        new_node = Node(data)
        new_node.next = self.root
        new_node.prev = None

        if self.root is not None:
            self.root.prev = new_node
        self.root = new_node
    
    def insert(self, prev, data):
        if prev is None: #Checks if prev is NULL
            print("Node doesn't exist in the List")
            return

        new_node = Node(data)
        new_node.next = prev.next #point next of new node as next of previous node 
        prev.next = new_node #next of previous as new node
        new_node.prev = prev #make previous as previous of new node

        if new_node.next is not Node:
            new_node.next.prev = new_node
    
    def append(self, data):
        new_node = Node(data)
        #traverses list until it reaches the last node
        current = self.root
        while current.next is not None:
            current = current.next
        current.next = new_node #changes the next of last
        new_node.prev = current #makes the last node the previous node

    def returnList(self, node):
        elements = []
        while node is not None:
            elements.append(node.data)
            node = node.next
        return elements 

newList = doublyLinkedList()
newList.append(8)
newList.append(66)
newList.append(77)
print(newList.returnList(newList.root))
newList.push(133)
print(newList.returnList(newList.root))
newList.insert(newList.root.next, 9)
print(newList.returnList(newList.root))