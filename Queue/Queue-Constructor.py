#Creating a node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value):
        new_node = Node(value) #creating a node
        #pointing the first & last to the new node
        self.first = new_node 
        self.last = new_node
        self.length = 1
    
    #Prints the queue untill it finds None
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

#Creates a queue with node 4
my_queue = Queue(4)

my_queue.print_queue()
