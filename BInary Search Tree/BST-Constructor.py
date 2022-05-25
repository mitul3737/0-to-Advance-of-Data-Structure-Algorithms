class Node:
    #creating a node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None #Creating an empty BInary Search Tree

#Creating a Binary Search Tree
my_tree = BinarySearchTree()

print(my_tree.root)


 