#increment/decrement counts
#O(n) time complexity
#O(n+m) space complexity, i think :(, not fully sure
#took 22 min
def kanagram(str1, str2, k):
    """
    Determines if str1 and str2 can be turned into anagrams with k or less character flips

    Inputs:
    str1: a string
    str2: a string
    k: an integer

    Output:
    True if str1 and str2 are kanograms, false otherwise
    """
    if len(str1) != len(str2):
        return False
    counter = {}
    #The counter will map each character in both str1 and str2 two the number of occurences of that character
    #in str1 minus the number of occurences of it in str2
    for char in str1:
        counter[char] = 0
    for char in str2:
        counter[char] = 0
    for char in str1:
        counter[char] += 1
    for char in str2:
        counter[char] -= 1
    letter_diff = 0
    for letter in counter:
        letter_diff += abs(counter[letter])
        #letter_diff will measure the total difference in characters between the two strings
    print(counter)
    if letter_diff <= 2*k:
        #each flip will account for 2 differences between the two strings
        return True
    else:
        return False
"""
print(kanagram("apple", "peach", 2))
print(kanagram("debit curd", "bad credit",1))
print(kanagram("abcdef", "abbbef",2))
print(kanagram("", "",0))
print(kanagram("cat", "dog",3))
"""

