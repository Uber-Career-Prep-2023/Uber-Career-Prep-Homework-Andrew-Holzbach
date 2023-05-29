"""
This problem can likely be solved using a heap/priority queue. You could initialize a heap of size k, and incrementally
add elements from the three lists so that you are always working with the k smallest elements from the lists.
"""

def merge_k(k,arrs):
    total_min_array = []
    min_heap = heap()
    for arr_num in range(k):
        if len(arrs[arr_num]) > 0:
            min_heap.insert((arr_num, 0, 0)) #heap elements are sorted by there value in the third idx, the first 2 represent the array and idx they come from
    while len(min_heap.array) != 0:
        min_val_info = min_heap.array[0]
        min_heap.remove()
        min_val = min_val_info[2]
        next_val_idx = min_val_info[1] + 1
        next_val_arr = min_val_info[0]
        total_min_array.appnd(min_val)
        if next_val_idx < len(next_val_arr):
            min_heap.insert((next_val_arr, next_val_idx, arrs[next_val_arr][next_val_idx]))
    return total_min_array
#Didn't have time to finish this but if you had a proper heap implementation it should work