class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        #For 0 items in list
        if self.length == 0:
            return None
        temp = self.tail
        #For 1 items in list
        if self.length == 1:
            self.head = None
            self.tail = None 
        #For more than 1 nodes in list
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
  
#Creates a list of Node 1 & Node 2

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)


# (2) Items - Returns  Node 2
print(my_doubly_linked_list.pop())
# (1) Item -  Returns  Node 1
print(my_doubly_linked_list.pop())
# (0) Items - Returns  None
print(my_doubly_linked_list.pop())

