#sort, then solve
#O(nlogn) time complexity
#O(1) space complexity
#took 32 minutes
def mergeintervals(intervals):
    """
    Inputs:
    Intervals: an array holding various pairs 
    """
    intervals.sort()
    #above will sort the pairs by their first values
    idx = 0
    while idx < len(intervals) - 1:
        #we want to look at each interval in order from least to greatest start and compare it to the next.
        if intervals[idx][1] >= intervals[idx+1][0] and intervals[idx][1] <= intervals[idx+1][1]:
            #if any next interval starts at an earlier value than the end of its previous interval, they can be merged
            intervals[idx] = (intervals[idx][0], intervals[idx+1][1])
            intervals.pop(idx+1)
        elif intervals[idx][1] >= intervals[idx+1][1]:
            #otherwise if the next interval is equivelent or held "within" the previous interval, merging them will be
            #equivalent to just getting rid of the next interval
            intervals.pop(idx+1)
        else:
            #we only move onto the next interval if we cannot merge the two intervals we are looking at
            idx += 1
        #print(intervals)
        #print(new_intervals)
    return intervals

"""
print(mergeintervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))
print(mergeintervals([(5, 8), (6, 10), (2, 4), (3, 6)]))
print(mergeintervals([(10, 12), (5, 6), (7, 9), (1, 3)]))
print(mergeintervals([(-10,1),(1,2),(2,3)]))
print(mergeintervals([(2,2),(2,2)]))
print(mergeintervals([]))
print(mergeintervals([(0,0)]))
"""