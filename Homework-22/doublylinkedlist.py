class Node:
    #Unless otherwise noted, functions are O(1)
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return self.head
    
    def insertAtBack(self,val):
        #O(n)
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            end_node = self.head
            while end_node.next != None:
                #this look moves end_node to the end of the LinkedList
                end_node = end_node.next
            end_node.next = new_node
            new_node.prev = end_node

    def insertAfter(self,val,loc):
        #O(n)
        new_node = Node(val)
        if loc is None:
            return "loc not in LinkedList"
        else:
            loc.next.prev = new_node
            new_node.next = loc.next
            new_node.prev = loc
            loc.next = new_node

    def deleteFront(self):
        #O(1)
        self.head = self.head.next
        self.head.prev = None
        return self.head
    
    def deleteEnd(self):
        #O(n)
        end_node = self.head
        while end_node.next != None:
            #this look moves end_node to the end of the LinkedList
            prev_node = end_node
            end_node = end_node.next
        prev_node.next = None

    def deleteNode(self, loc):
        #O(n)
        if loc == self.head:
            return self.deleteFront()
        pre_loc = self.head
        while pre_loc.next != None:
            if pre_loc.next == loc:
                pre_loc.next == loc.next
                return self.head
            else:
                pre_loc = pre_loc.next
        return "loc not in LinkedList"
            
    def length(self):
        #O(n)
        count = 0
        end_node = self.head
        while end_node != None:
            #this look moves end_node to the end of the LinkedList
            count += 1
            end_node = end_node.next
        return count
    
    def reverseIterative(self):
        #O(n)
        cur_node = self.head
        if cur_node == None:
            return "List Length 0, reversal yields same linked list"
        if cur_node.next == None:
            return "List Length 1, reversal yields same linked list"
        while cur_node != None:
            #this loop reverses the "arrow" for each two connected nodes
            #besides the tail, which is done outside of the loop     
            prev_node = cur_node.prev #None
            next_node = cur_node.next #4
            cur_node.next = prev_node
            cur_node.prev = next_node
            cur_node = next_node
        self.head = prev_node.prev

    def reverseRecursive(self):
        if self.head == None:
            return "done"
        original_head = self.head
        self.reverseRecursivehelper()
        original_head.next = None


    def reverseRecursivehelper(self):
        if self.head.next == None:
            cur_node = self.head
            prev_node = cur_node.prev
            cur_node.next = prev_node
            cur_node.prev = None
        else:
            cur_node = self.head
            prev_node = self.head.prev
            next_node = self.head.next
            self.head = next_node
            self.reverseRecursivehelper()
            cur_node.next = prev_node
            cur_node.prev = next_node

    def printList(self):
        #Testing Function
        lst = []
        end_node = self.head
        while end_node != None:
            lst.append(end_node.data)
            end_node = end_node.next
        print(lst)

l = LinkedList()
l.insertAtFront(5)
l.insertAtFront(4)
l.insertAtFront(10)
l.insertAtFront(20)
l.insertAfter(23, l.head)
l.printList()
l.reverseRecursive()
l.printList()
l.reverseIterative()
l.printList()