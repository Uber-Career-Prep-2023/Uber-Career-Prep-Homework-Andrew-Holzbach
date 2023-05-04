class Node:

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def min(self):
        node = self.root
        while node.left != None:
            node = node.left
        return node.data
    
    def max(self):
        node = self.root
        while node.right != None:
            node = node.right
        return node.data
    
    def contains(self, val):
        if self.data == val:
            return True
        elif self.data == None:
            return False
        elif self.data > val:
            return self.right.contains(val)
        elif self.data < val:
            return self.left.contains(val)
        
    def insert(self, val):
        if self.data > val:
            if self.right == None:
                self.right = Node(val)
            else:
                self.right.insert(val)
        elif self.data < val:
            if self.left == None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            self.data = val
