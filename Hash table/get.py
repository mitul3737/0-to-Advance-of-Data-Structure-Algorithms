class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    

    #creating the get method
    def get_item(self, key):
        index = self.__hash(key) #looks for the index of the key
        if self.data_map[index] is not None: #if there is an array within the array, it will return the value
            for i in range(len(self.data_map[index])): #loops through the array and sets value for i using the length of it
                if self.data_map[index][i][0] == key: #if it founds the key, sends the value of it
                    return self.data_map[index][i][1]
        return None #else returns none as nothing is out there
             

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

#check for values using key 
print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))
