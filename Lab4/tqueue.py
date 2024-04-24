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


class CircledQueueArray:
    def __init__(self, length=10, head_index=0, tail_index=0):
        self.set = ["#"]*length
        self.head=head_index
        self.tail=tail_index

    def add(self, value):
        if(self.tail==self.head and self.set[self.tail]!='#'):
            print('Queue already full')
            return
        self.set[self.tail]=value
        self.tail+=1
    
    def get(self):
        val = self.set[self.head]
        self.set[self.head]='#'
        self.head+=1
        return val
    
    def __str__(self):
        return str(self.set)    

