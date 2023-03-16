#Growing Shrinking sliding window
#
# 40 minutes not complete
def shortestsub(string, req_chars):
    ptr1 = 0
    ptr2 = 0
    current_sub = ""
    smallest_sub = len(string)
    for char in req_chars:
        #check if all req_chars are in string bc no substring has more characters that it's string
        if char not in string:
            return None
    while ptr2 <= len(string) - 1:
        for char in req_chars:
            #moves ptr2 forwards until our window includes every required character
            while char not in current_sub:
                ptr2 += 1
                current_sub = string[ptr1:ptr2+1]
        #window initially must be valid but in next look we will check the window after each ptr1 move to make sure it is still valid
        valid = True
        while ptr1 != ptr2:
            current_sub = string[ptr1:ptr2+1]
            #print(current_sub)
            for char in req_chars:
                if char not in current_sub:
                    valid = False
                if valid and len(current_sub) < smallest_sub:
                    smallest_sub = len(current_sub)
            ptr1 += 1
        #print(smallest_sub)
    return smallest_sub
    
print(shortestsub("abracadabra", "abc"))