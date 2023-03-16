#Hash the running computation
#O(n) time complexity
#O(n) space complexity
#not finished after 40 min
def zerosum(arr):
    """
    Finds the number of subarrays in arr which sum to zero

    Inputs:
    arr: an array of integers
    
    Output:
    The number of subarrays in arr which sum to zero
    """
    n = len(arr)
    total_sum = sum(arr)
    num_subs = 0
    sums = []
    if n == 0:
        return 0
    sums.append(total_sum)
    if total_sum == 0:
        num_subs += 1
    for idx in range(0, n-1):
        #runs through each arr created by removing rightmost element
        next_sum = sums[-1] - arr[idx]
        sums.append(next_sum)
        if next_sum == 0:
            num_subs += 1
            print(next_sum)
    sums = sums[:0]
    for idx in range(n-1, 0):
        #runs through each arr created by removing leftmost element
        next_sum = sums[-1] - arr[idx]
        sums.append(next_sum)
        if next_sum == 0:
            num_subs += 1
    sums = sums[:0]
    for idx in range(0, int(n/2-1)):
        print(idx)
        #runs through each arr created by removing both leftmost and rightmost element
        next_sum = sums[-1] - arr[idx] - arr[-idx -1]
        if next_sum == 0:
            num_subs += 1
    return num_subs

print(zerosum([1,2,3,4,-4,10]))