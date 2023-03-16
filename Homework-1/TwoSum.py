#sort, then solve, and forward/backward two pointer
#O(nlogn) time complexity
#O(1) Space complexity
#Took 40 minutes
def twosum(lst, k):
    """
    Returns the number of unique pairs in lst which sum to k.

    Inputs: 
    lst: an array of integers
    k: an integer

    Output:
    The integer number of pairs in lst which sum to k.
    """
    ptr1 = 0
    ptr2 = len(lst) - 1
    lst.sort()
    sum_count = 0
    while ptr1 < ptr2:
        #print(ptr1, ptr2, lst)
        if lst[ptr1] + lst[ptr2] == k:
            #if the two elements we look at add up to k, we want to increase how many pairs we know sum to k
            sum_count += 1
            while lst[ptr1+1] == lst[ptr1]:
                #this is in case the same next ptr1 is the same, ptr1+1 and ptr2 will be another valid pair
                ptr1 += 1
                sum_count += 1
            if ptr1 < ptr2:
                #we need to check again whether the pointers are the same
                while lst[ptr2-1] == lst[ptr2]:
                    #this is in case the next ptr2 is the same, ptr1 and ptr2-1 will be another valid pair
                    ptr2 -= 1
                    sum_count += 1
            ptr1 += 1 
            ptr2 -= 1
        elif lst[ptr1] + lst[ptr2] > k:
            #because lst is sorted, we know to move ptr2 left when the sum is greater than k
            ptr2 -= 1
        elif lst[ptr1] + lst[ptr2] < k:
            ptr1 += 1
    return sum_count

"""
print(twosum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10))
print(twosum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 9))
print(twosum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6))
print(twosum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1))
print(twosum([1,0,0,0,0],1))
print(twosum([],1))
"""