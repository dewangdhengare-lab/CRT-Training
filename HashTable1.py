#Linear +Probing
class HashTable:
    def __init__(self,size):
        self.size =size
        #self.table - [[] for i in range(size)]
        self.table = [None]*size

    def hash_function(self,key):
        return key% self.size
    def insert(self,key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = key
    def display(self):
            print(self.table)

h = HashTable(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()