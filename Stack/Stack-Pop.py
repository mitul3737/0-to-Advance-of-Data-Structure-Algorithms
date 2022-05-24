class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        #when we have no nodes in the stack
        if self.height == 0:
            return None
        #when we have nodes in the stack
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
#A stack of nodes 7,23,3,11

my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

#poping a node from the stack. Note: pop returns the last value intered into the stack[last in first out]
print(my_stack.pop(), '\n')

my_stack.print_stack()
