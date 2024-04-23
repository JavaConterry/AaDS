import sys
sys.path.append('C:\\Users\\glebo\\Documents\\University\\AaDS')

from Lab3.LinkedList import BiLinkedList

class Stack_List:
    def __init__(self):
        self.list = BiLinkedList()

    def add(self, value):
        self.list.addLast(value)
    
    def get(self):
        return self.list.takeLast()
    
    def __str__(self):
        return str(self.list)


class Stack_Array:
    def __init__(self):
        self.set = []

    def add(self, value):
        self.set.append(value)
    
    def get(self):
        val = self.set.pop(len(self.set)-1)
        return val
    
    def __str__(self):
        return str(self.set)    
    

# class Queue_Array:
#     def __init__(self):
#         self.set = []

#     def add(self, value):
#         self.set.append(value)
    
#     def get(self):
#         val = self.set[0]
#         self.set.remove(val)
#         return val
    
#     def __str__(self):
#         return str(self.set)    