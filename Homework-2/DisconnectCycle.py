#Took 15 minutes
#hashing the linked list
#O(n) time complexity, O(n) Space Complexity

import singlylinkedlist as sinll

def disconnect_cycle(sll):
    node = sll.head
    if node == None or node.next == None:
        return sll
    visited = set() #hashset for nodes we have already seen
    while node.next != None: #if we reach the tail of the sll, there is no longer a cycle or never was one
        visited.add(node)
        print(visited)
        print(node.data)
        if node.next in visited:
            node.next = None
            break #if the next node has already been visited, we are at what should be the tail of the sll
        else:
            node = node.next
    return sll
"""
sll0 = sinll.LinkedList()
sll0.insertAtBack(10)
sll0.insertAtBack(18)
sll0.insertAtBack(12)
sll0.insertAtBack(9)
sll0.insertAtBack(11)
sll0.insertAtBack(4)
actual_head = sll0.head
sll0.reverseIterative()
actual_tail = sll0.head
sll0.reverseIterative()
print(actual_tail.next)
print(actual_head.next.data)
actual_tail.next = actual_head.next
print(actual_tail.next.data)
disconnect_cycle(sll0)
sll0.printList()
"""