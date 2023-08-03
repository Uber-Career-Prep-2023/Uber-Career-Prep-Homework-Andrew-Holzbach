# Using: Trie as a parameter(the dictionary of terms can be inputted as a Trie) and bfs
# Stuck after 40 minutes :(

def boggle(dictionary, board):
    """
    Inputs: dictionary - a trie representing the terms to be found on the board
            board - an array of arrays representing the matrix board of characters
    """
    ret_set = set()
    children = dictionary.children()
    for letter in children:
        if children[letter] != None:
            for i in len(board):
                for j in len(board[0]):
                    if board[i][j] == letter:
                        
def bfs(i,j,word,board,dictionary,ret_set):
    """
    This function is intended to find all valid words starting from (i,j)
    """
    moves = [(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1),(1,0),(0,1),(1,1)]
    visited = set()
    queue = [(i,j,word)]
    while queue:
        current = queue.pop(0)
        if current[0]<len(board) and current[1]<len(board[1]):
            visited.add(current)
            for letter in dictionary:
                if dictionary.valid_word():
                    ret_set.add(word+letter)
                if dictionary[letter] != None:




        


