"""
Using: Tabulation

Took 40 minutes
"""

def largest_1square(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return "Not Square"
    max_size = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i>0 and j>0:
                if matrix[i][j] == 1:
                    square = min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1])+1
                    #print(square)
                    matrix[i][j] = square
                    if square > max_size:
                        max_size = square
    #print(matrix)
    return max_size
    
tests = [([[1,1],[1,1]],2),
         ([[0,1,0,1],[0,0,1,1],[0,1,1,1],[0,0,1,1]],2),

         ]

for test in tests:
    if largest_1square(test[0]) == test[1]:
        print(True, test)
    else:
        print(False, test)