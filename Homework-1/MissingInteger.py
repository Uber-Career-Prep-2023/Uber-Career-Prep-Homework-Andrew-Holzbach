#binary search variation
#O(logn) time complexity
#O(1) space complexity
#took 30 minutes
def missingint(lst, num):
    """
    Finds the missing integer in a sorted list of integers from 1-n

    Inputs: 
    lst: a sorted array of integers of size n-1
    num: an integer

    Output:
    The missing integer
    """
    if num == 1:
        return 1
    if lst[0] != 1:
        return 1
    if lst[-1] != num:
        return num
    #The above statements are edge cases for when the missing integer is the first or last element of the array
    low = 0
    high = num - 1
    while high >= low:
        mid = low + (high-low)//2 
        #print(mid)
        #we choose mid to be the center element of the array
        if lst[mid] == lst[mid-1] + 2:
            #if the mid element is the element before the skipped element, return the skipped element
            return lst[mid] - 1
        elif lst[mid] == mid+1:
            #if the mid element is "correct" for its position, the skipped element must be later in the list
            low = mid + 1
        else:
            #the remaining option is that the skipped element is before mid
            high = mid - 1
"""
print(missingint([1,2,3,5,6,7],7))
print(missingint([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12],12))
print(missingint([1],2))
print(missingint([],1))
print(missingint([2],2))
print(missingint([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,14],14))
"""