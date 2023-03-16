#growing shrinking sliding window
#O(n) time complexity
#O(1) space complexity
#took 40 min
def deduparr(lst):
    """
    Removes repeated numbers from an array

    Input:
    lst: a sorted array of nonegative integers

    Output:
    The same lst with the repeat elements removed
    """
    idx1 = 0
    idx2 = 0
    length = len(lst)
    if length == 0 or length == 1:
        return lst
    while idx2 < length-1:
        #idx2 of lst moves forward each iteration and its value assigns to idx1 of lst whenever you reach
        #non-repeat numbers, then idx1 moves forwards again
        if lst[idx2] != lst[idx2+1]:
            lst[idx1] = lst[idx2]
            idx1 += 1
            idx2 += 1
        else:
            idx2 += 1
        #print(lst, idx1, idx2)
    lst[idx1] = lst[idx2]
    for idx in range(length -1, idx1 , -1):
        #print(lst)
        lst.pop(idx)
    return lst
"""
print(deduparr([1,1,2,3,3,4,5,5]))
print(deduparr([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]))
print(deduparr([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
print(deduparr([1, 3, 4, 8, 10, 12]))
print(deduparr([]))
print(deduparr([1,1]))
print(deduparr([4,5]))
"""