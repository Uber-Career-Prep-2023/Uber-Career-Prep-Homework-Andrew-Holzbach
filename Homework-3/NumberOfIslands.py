#You could reason about this as a graph problem, where nodes exist on the entries with 1, and there
#are edges between entries in the matrix adjacent to each other, we could then traverse through each island
#to count the number of disconnected "pieces" of the graph/matrix
# O(n*m) time complexity not sure space complexity due to recursion
#took 37 minutes

def num_islands(matrix):
    m = len(matrix) # m is set to the number of rows in matrix
    if m == 0:
        return 0 
    n = len(matrix[0]) # n is set to the number of columns in matrix
    visited_nodes = set()
    island_count = 0
    for i in range(0,m):
        for j in range(0,n):
            if matrix[i][j] == 1:
                if (i,j) not in visited_nodes:
                    island_count += 1
                    search_island(matrix, visited_nodes, i, j, m, n) #adds each node in (i,j)'s island to visited_nodes
    return island_count
                    
                    
def search_island(matrix, visited_nodes ,i ,j , m, n): #ends when the entire island has been traversed
    if (i,j) not in visited_nodes:
        visited_nodes.add((i,j))
        if matrix[i][j] == 1:
            if i > 0:
                search_island(matrix, visited_nodes, i-1, j, m, n) 
            if i < m-1:
                search_island(matrix, visited_nodes, i+1, j, m, n)
            if j > 0:
                search_island(matrix, visited_nodes, i, j-1, m, n)
            if j < n-1:
                search_island(matrix, visited_nodes, i, j+1, m, n)
    return None

matrix1 = [[1,0,1,1,1],[1,1,0,1,1],[0,1,0,0,0],[0,0,0,1,0],[0,0,0,0,0]]
print(num_islands(matrix1))
matrix2 = [[1,0,0],[0,0,0]]
print(num_islands(matrix2))