#Node class : Creates node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
#Creates a stack class
class Stack:
    def __init__(self, value):
        #creates a node by calling the Node class
        new_node = Node(value)
        #pointing the top to that node
        self.top = new_node
        #adding the length to 1
        self.height = 1
    #Prints the stack untill it finds None
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

#Creating a stack with node 4
my_stack = Stack(4)

#Printing the stack
my_stack.print_stack()

