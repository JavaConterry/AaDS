import sys
sys.path.append('C:\\Users\\glebo\\Documents\\University\\AaDS')

from Lab3.LinkedList import BiLinkedList


class Queue_List:
    def __init__(self):
        self.list = BiLinkedList()

    def add(self, value):
        self.list.addLast(value)
    
    def get(self):
        return self.list.takeFirst()
    
    def __str__(self):
        return str(self.list)


class Queue_Array:
    def __init__(self):
        self.set = []

    def add(self, value):
        self.set.append(value)
    
    def get(self):
        val = self.set.pop(0)
        return val
    
    def __str__(self):
        return str(self.set)    