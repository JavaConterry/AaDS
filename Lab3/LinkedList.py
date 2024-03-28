class Node:
    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous
    
    def hasNext(self):
        if(self.next != None):
            return True
        return False

    
    def hasPrevious(self):
        if(self.previous != None):
            return True
        return False



class BiLinkedList:    #     head -> .... -> tail
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def addLast(self, e):
        node = Node(e)
        if(self.length == 0):
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail ###
            self.tail.next = node
            self.tail = node
        self.length+=1
    
    def addFirst(self, e):
        node = Node(e)
        if(self.length == 0):
            self.head = node
            self.tail = node
        else:
            # prev_head_link = self.head ###
            # self.head.previous = node ###
            node.next = self.head  
            node.next.previous = node ###
            # node.next = prev_head_link ###
            self.head = node
        self.length+=1
    
    def add(self, index, e):
        if(index < 0):
            return
        if(index == 0):
            self.addFirst(e)
            return
        if(self.length <= index):
            self.addLast(e)
            return

        current = self.head
        while(index-2>0):              # (1)0_(2)1_2_3_4
            current.previous = current ###
            current = current.next
            index-=1

        current.next = Node(e, current.next, current) ### current
        self.length+=1
    
    def __str__(self):
        output = ""
        current = self.head
        output += str(current.value)
        while(current.hasNext()):
            current = current.next
            output += " "+str(current.value)
        return output
    
    def takeFirst(self):
        if(self.length==0):
            return
        val = self.head.value
        self.head = self.head.next
        self.head.previous = None ###
        self.length -=1
        return val

    def takeLast(self):
        if(self.length==0):
            return
        val = self.tail.value
        current = self.head
        i=1
        while(i<self.length-1):
            current = current.next
            i+=1
        current.next = None
        self.tail = current
        self.length -=1
        return val
    
    def remove(self, index):
        if(self.length==0):
            return
        if(index>=self.length):
            return self.takeLast()

        current = self.head
        while(index-2>0):
            current = current.next
            index-=1    
        val = current.next.value
        current.next = current.next.next
        current.next.previous = current ###
        if current.next == None:
            self.tail = current
        self.length -=1
        return val
    
    def set(self, e, index):
        if(self.length==0):
            return
        if(index>self.length):
            self.addLast(Node(e))

        current = self.head
        while(index-1>0):
            current = current.next
            index-=1
        current.value = e
    
    def get(self, index):
        if(index > self.length):
            return
        current = self.head
        while(index-1>0):
            current = current.next
            index-=1
        return(current.value)

    def read(self, text_set):
        addtext = ''
        for i in text_set:
            if(i != ' ' and i != '.'):
                addtext += i
            else:
                self.addLast(addtext)
                addtext = ''