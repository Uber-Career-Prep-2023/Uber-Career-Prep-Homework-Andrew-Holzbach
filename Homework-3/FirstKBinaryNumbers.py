#took 36 minutes, used queue within bin_nums_queue with the pointer
#O(n) time and space complexity
def f_k_b_num(n):
    if n == 0:
        return []
    if n == 1:
        return ["0"]
    if n == 2:
        return ["0", "1"]
    ptr = 1
    bin_nums_queue = ["0", "1"]
    while len(bin_nums_queue) < n:
        prefix = bin_nums_queue[ptr]
        bin_nums_queue.append(prefix + "0")
        bin_nums_queue.append(prefix + "1")
        ptr += 1
    return bin_nums_queue

print(f_k_b_num(10))