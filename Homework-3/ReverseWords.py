"""
Could use stack structure by adding the words in forward order and then taking them out and appending to 
new array, thereby reversing.
Took 38 minutes
O(n) time and space complexity
"""
def reverse_words(words):
    if len(words) == 0:
        return ""
    if len(words) == 1 or len(words) == 2: #I am assuming here that there cannot be a space at the beginning or end of words
        return words
    stack = []
    last_space = 0
    for idx in range(0,len(words)):
        if words[idx] == " ":
            word = words[last_space:idx]
            stack.append(word)
            last_space = idx + 1
    stack.append(words[last_space:len(words)])
    print(words[last_space:len(words)])
    reversed_arr = []
    while len(stack) > 1:
        word = stack.pop()
        reversed_arr.append(word)
        reversed_arr.append(" ")
    reversed_arr.append(stack.pop())
    return "".join(reversed_arr)

print(reverse_words("a b"))
print(reverse_words("Emma lives in Brooklyn, New York."))

