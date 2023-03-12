#forward/backward two pointer
#O(n) time complexity
#O(n) space complexity
#Took 40 minutes
def reverse(str):
    """""
    Reverses the vowels of the input str and returns them in a new string.

    Inputs:
    str: a string of letters

    Outputs:
    swap_str: a string of the letters in str with the vowels reversed
    """""
    swap_list = list(str)
    vowels = {"a","e","i","o","u","A","E","I","O","U"}
    ptr1 = 0
    ptr2 = len(str) - 1
    while ptr1 < ptr2:
        #print(ptr1)
        #print(ptr2)
        if swap_list[ptr1] not in vowels:
            ptr1 += 1
        if swap_list[ptr2] not in vowels:
            ptr2 -= 1
        if swap_list[ptr1] in vowels and swap_list[ptr2] in vowels:
            vow1 = swap_list[ptr1]
            vow2 = swap_list[ptr2]
            swap_list[ptr1] = vow2
            swap_list[ptr2]= vow1 
            ptr1 += 1
            ptr2 -= 1
        #print(swap_list)
    swap_str = ""
    for char in swap_list:
        swap_str = swap_str + char
    return swap_str
"""""
print(reverse("Hi Andrew"))
print(reverse(""))
print(reverse("ae"))
print(reverse("xyz"))
print(reverse("Uber Career Prep"))
print(reverse("flamingo"))
"""""