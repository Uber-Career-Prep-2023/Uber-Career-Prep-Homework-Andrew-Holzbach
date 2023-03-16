#Simultaneous Iteration Two Pointer
#O(n+m) time complexity where n and m are the lengths of the two strings
#O(1) space complexity
#took 40 minutes
def backstringcompare(str1, str2):
    """
    Function which tells if two strings are the same regardless of keystroke(after # backspaces).

    Inputs: 
    str1: a string
    str2: a string

    Output: 
    True or False depending on if the strings are the same after backspaces.
    """
    ptr_1 = len(str1)-1
    ptr_2 = len(str2)-1
    #the pointers start from the left of the stings and iterate backwards
    while ptr_1 >= 0 and ptr_2 >= 0:
        if str1[ptr_1] == "#":
            #counts #'s and skips that many next left characters
            skip_count = 0
            while str1[ptr_1] == "#":
                print(ptr_1)
                skip_count += 1
                ptr_1 -= 1
            while skip_count > 0:
                skip_count -= 1
                ptr_1 -= 1
        if str2[ptr_2] == "#":
            skip_count = 0
            while str2[ptr_2] == "#":
                skip_count += 1
                ptr_2 -= 1
            while skip_count > 0:
                skip_count -=1
                ptr_2 -= 1
        if str1[ptr_1] != str2[ptr_2]:
            return False
        if str1[ptr_1] == str2[ptr_2]:
            ptr_1 -= 1
            ptr_2 -= 1
        #print(ptr_1, ptr_2)
    return True
"""
print(backstringcompare("abc","abc"))
print(backstringcompare("Uber Career Prep", "u#Uber Careee#r Prep"))
print(backstringcompare("abcdef###xyz", "abcdefxyz###"))
print(backstringcompare("a#", ""))
print(backstringcompare("", ""))
print(backstringcompare("abcdef###xyz", "abcw#xyz"))
"""