class BinaryTree:
    def __init__(self, value=0, leteral=False):
        self.value=value
        self.left=None
        self.right=None
        self.leteral=leteral
    
    def add(self, value):      
        if(value<=self.value):
            if(self.left==None):
                self.left=BinaryTree(value)
            else:
                self.left.add(value)
        if(value>self.value):
            if(self.right==None):
                self.right=BinaryTree(value)
            else:
                self.right.add(value)
        
    def find(self, value, level=0):
        if value==self.value: 
            return value, level            
        elif(value<self.value): return self.left.find(value, level=level+1)
        elif(value>self.value): return self.right.find(value, level=level+1)

        # default return
        print('object not found') 
        return
    
    def find_node(self, value):
        if value==self.value: 
            return value            
        elif(value<self.value): return self.left.find(value)
        elif(value>self.value): return self.right.find(value)

        # default return
        print('object not found') 
        return


    def remove(self, value):
        self.__remove_node(value)

    def __remove_node(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.__remove_node(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.__remove_node(value, self)
        else:
            # node has two children
            if self.left is not None and self.right is not None:
                successor = self.right.find_min()
                self.value = successor.value
                self.right.__remove_node(successor.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    # single node tree
                    self.value = None
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current


    def __str__(self, array=False):
        if(array):
            arr = []
            if self.left != None:
                arr.extend(self.left.__str__(array=True))
            arr.extend(str(self.value))
            if self.right != None:
                arr.extend(self.right.__str__(array=True))
            return arr
        else:
            result = ''
            if self.left != None:
                result += str(self.left)
            result += str(self.value) + ' '
            if self.right != None:
                result += str(self.right)
            return result

    def pretty_print(self):
        self.__print_tree_helper()

    def __print_tree_helper(self, node=None, level=0):
        if node is None:
            node = self
        if node.right:
            self.__print_tree_helper(node.right, level + 1)
        print('    ' * level + str(node.value))
        if node.left:
            self.__print_tree_helper(node.left, level + 1)