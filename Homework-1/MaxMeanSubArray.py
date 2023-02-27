#Fixed size sliding window
#O(nk) Time Complexity
#O(n) Space Complexity
#Took 35 minutes
def MaxMeanSubArray(arr, k):
    """
    Returns the subarray of arr of size k which has the largest mean.

    Inputs: 
    arr: an array of integers
    k: an integer

    Output:
    Highest subarray mean
    """
    if len(arr) == 0 or k == 0:
        return None
    elif  len(arr) < k:
        return "Error"
    largest_mean = -float('inf')
    for pointer1 in range(len(arr) - k+1):
        #pointer1 tracks the first element of our window
        #print(pointer1)
        pointer2 = pointer1 + k
        #pointer2 tracks the second element of our window
        sum = 0
        for ptr in range(pointer1, pointer2):
            #this loop sums up the elements of each size k window
            sum = sum + arr[ptr]
        mean = sum/k
        if mean > largest_mean:
            largest_mean = mean
    return largest_mean

#print(MaxMeanSubArray([0],0))
#print(MaxMeanSubArray([4,5,-3,2,6,1],2))
#print(MaxMeanSubArray([2,3],2))
#print(MaxMeanSubArray([1,1,1,1,-1,-1,2,-1,-1],3))
