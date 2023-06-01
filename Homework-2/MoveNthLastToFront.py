#Took 20 minutes
#Fixed distance two pointer
#O(n) time complexity, O(1) space complexity

import singlylinkedlist as sinll

def nth_to_front(sll,k):
    front = sll.head
    if front == None:
        if k == 0:
            return sll
        else:
            return "Length of list less than k"        
    elif front.next == None:
        if k == 1:
            return sll
        else:
            return "Length of list less than k"   
    for _ in range(k): # this initializes the front pointer to be k ahead of the rear pointer
        if front == None:
            return "Length of list less than k"
        front = front.next
    rear = sll.head
    if front != None:
        while front.next != None: #this pushes both front to the end of the sll while maintaining rear k behind it
            front = front.next
            rear = rear.next
    new_head = rear.next
    rear.next = rear.next.next
    new_head.next = sll.head
    sll.head = new_head
    return sll

my_sll = sinll.LinkedList()
my_sll.insertAtBack(15)
my_sll.insertAtBack(2)
my_sll.insertAtBack(8)
my_sll.insertAtBack(7)
my_sll.insertAtBack(20)
my_sll.insertAtBack(9)
my_sll.insertAtBack(11)
my_sll.insertAtBack(6)
my_sll.insertAtBack(19)
my_sll.printList()
nth_to_front(my_sll, 2)
my_sll.printList()
my_sll0 = sinll.LinkedList()
my_sll0.insertAtFront(1)
my_sll0.insertAtFront(2)
nth_to_front(my_sll0,2)
my_sll0.printList()