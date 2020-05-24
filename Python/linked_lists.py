class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.root = Node()
        self.size = 0
    def get_size(self):
        curr = self.root
        counter = 0 
        while curr.next is not None:
            counter += 1 
            curr = curr.next
        return counter
    def add(self, data):
        new_node = Node(data)
        curr = self.root
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
    def returnList(self):
        elements = []
        curr_node = self.root
        while curr_node.next is not None:
            curr_node = curr_node.next
            elements.append(curr_node.data)
        return elements 
    def find(self, index):
        if index >= self.get_size():
            print ("Out of bounds error!")
            return None
        curr_node = self.root 
        curr_index = 0 
        while curr_node:
            curr_node = curr_node.next
            if curr_index == index:
                return curr_node.data
                curr_index += 1
    
    def remove(self, data):
        curr_node = self.root
        prev_node = None
        while curr_node:
            if curr_node.data == data:
                if prev_node:
                    prev_node.next = curr_node.next
                else:
                    self.root = curr_node
                self.size -= 1
                return True #data is found
            else:
                prev_node = curr_node
                curr_node = curr_node.next
        return False #data isn't found



# Remove not working
newList = LinkedList()
newList.add(8)
newList.add(66)
newList.add(77)
newList.add(2)
newList.add(5)
print(newList.returnList())
print(newList.remove(5))
print(newList.returnList())
