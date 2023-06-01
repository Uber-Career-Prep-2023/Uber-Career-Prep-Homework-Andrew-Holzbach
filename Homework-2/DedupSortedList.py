# 20 minutes
#fixed-distance two-pointer
# O(n) time complexity, O(1) space complexity
import singlylinkedlist
def dedupSL(sll):
    if sll.head == None:
        return sll
    elif sll.head.next == None:
        return sll
    else:
        cur_node = sll.head
        while cur_node.next != None:
            next_node = cur_node.next
            if next_node.data == cur_node.data:
                cur_node.next = next_node.next
            else:
                cur_node = cur_node.next
        return sll

"""
l = singlylinkedlist.LinkedList()
l.insertAtFront(5)
l.insertAtFront(4)
l.insertAtFront(10)
l.insertAtFront(10)
l.insertAtFront(20)
l.insertAtFront(20)
l.insertAtFront(20)
l.printList()
dedupSL(l).printList()
"""