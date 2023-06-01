#took 8 minutes
#forward-backward 2 pointer
#O(n) time complexity, O(1) space complexity
import doublylinkedlist as doull

def is_palindrome(dll):
    ptr1 = dll.head
    ptr2 = dll.head
    if ptr1 == None or ptr1.next == None:
        return True
    while ptr2.next != None: # Move ptr2 to be at the end of the doubly linked list
        ptr2 = ptr2.next
    while ptr1 != ptr2 and ptr1.next != ptr2: # move the two ptrs together until they are at the same spot or adjacent
        if ptr1.data != ptr2.data:
            return False
        else:
            ptr1 = ptr1.next
            ptr2 = ptr2.prev
    return True
"""
my_dll = doull.LinkedList()
my_dll.insertAtBack(9)
my_dll.insertAtBack(2)
my_dll.insertAtBack(4)
my_dll.insertAtBack(2)
my_dll.insertAtBack(9)
print(is_palindrome(my_dll))
my_dll.deleteEnd()
print(is_palindrome(my_dll))
my_dll.deleteFront()
print(is_palindrome(my_dll))
my_dll0 = doull.LinkedList()
my_dll0.insertAtBack(1)
my_dll0.insertAtBack(2)
my_dll0.insertAtBack(2)
my_dll0.insertAtBack(1)
print(is_palindrome(my_dll0))
"""