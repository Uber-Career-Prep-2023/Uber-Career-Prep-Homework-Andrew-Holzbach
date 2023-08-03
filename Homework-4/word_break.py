"""
Using: Memoization
O(n^2) time complexity, O(n) space complexity
Took 38 minutes
"""
memo = set()
def word_break(dictionary, word):
    print(word)
    if len(word) == 0:
        return True
    ptr = 0
    while ptr<len(word):
        if word[0:ptr+1] in dictionary:
            remaining = word[ptr+1:-2]
            if remaining not in memo:
                if word_break(dictionary, remaining):
                    return True
                else:
                    memo.add(remaining)
        ptr+=1
    return False
                
diction = set(['elf','go','golf','man','manatee','not','note','pig'])
print(word_break(diction, 'mangolf'))
print(word_break(diction, 'manateenotelf'))
print(word_break(diction, 'quipig'))