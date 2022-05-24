class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    #Adding a node at last of queue    
    def enqueue(self, value):
        new_node = Node(value)
        #If there are no nodes in the queue
        if self.first is None:
            self.first = new_node
            self.last = new_node
        #If there are nodes in the queue    
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        
#Creating a queue with node 1
my_queue = Queue(1)
#Adding a node 2 at the last of queue
my_queue.enqueue(2)

my_queue.print_queue()
