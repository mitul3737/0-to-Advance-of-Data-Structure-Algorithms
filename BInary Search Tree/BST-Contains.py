class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        #Setting the root value as temp
        temp = self.root
        while (temp is not None):
            #Checks if the node is smaller than the temp node
            if value < temp.value:
                temp = temp.left
            #Checks if the node is bigger than the temp node    
            elif value > temp.value:
                temp = temp.right
            #Checks if the node is equal to temp node
            else:
                return True
        return False #When temp is None, it will return False
        


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

#Looking for 27 in the tree
print(my_tree.contains(27))


#Looking for 17 in the tree
print(my_tree.contains(17))
                
