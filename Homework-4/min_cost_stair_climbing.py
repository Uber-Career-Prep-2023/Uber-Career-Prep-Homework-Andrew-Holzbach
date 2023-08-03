"""
Using: Memoization
O(n) time complexity, O(n) space complexity
Took 30 minutes
"""

def min_cost(memo,stairs,n):
    """
    Input: memo - memoization dict, stairs: input step cost list

    Output: int - the minimum possible toll you can pay to stair n
    """
    #print(n, memo)
    if n == 0:
        return stairs[0]
    elif n == 1:
        return stairs[1]
    elif n in memo:
        return memo[n]
    else:
        minimum = stairs[n] + min(min_cost(memo,stairs,n-1),min_cost(memo,stairs,n-2))
        memo[n] = minimum
        return minimum
    
def total_min(stairs):
    if len(stairs) == 0 or len(stairs) == 1:
        return 0
    memo = {} 
    return min(min_cost(memo, stairs,len(stairs)-1), min_cost(memo, stairs, len(stairs)-2))
    

print(total_min([3,1,6,3,5,8]))
print(total_min([11,8,3,4,9,13,10]))

