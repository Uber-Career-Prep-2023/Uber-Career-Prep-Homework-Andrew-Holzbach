class Graph:

    def __init__(self,edges):
        self.graph = {}
        for edge in edges:
            #initializes each node as a key in the graph mapping to an empty list
            self.graph[edge[0]] = []
            self.graph[edge[1]] = []
        for edge in edges:
            #for each node which has outward facing edges, add the edges to it's adjacency list
            self.graph[edge[0]].append(edge[1])

    #   Not fully sure whether we are given a start node as part of the graph object, therefore
    #   the bottom 2 implementations runs bfs and dfs starting from every node in the graph, this would be
    #   how to determine if target is in the graph if a start node is not specified, this would be much faster with a specified start node

    def bfs(self, target):
        visited = set()
        for node in self.graph.keys(): #We are running bfs starting from each node in graph, this is necessary in a directed graph
            if node not in visited:  #If node is in visited, we know that every visitable node from it has already been treaversed
                #Below is a standard implementation of bfs from "node"
                queue = [node]
                while len(queue) > 0:
                    current = queue.pop()
                    if current not in visited:
                        visited.add(current)
                        if current == target:
                            return True
                        if current in self.graph:
                            for neighbor in self.graph[current]:
                                if neighbor not in visited:
                                        queue.insert(0,neighbor)
        return False

    def dfs(self,target):
        visited = set()
        for node in self.graph.keys():
            if node not in visited:
                stack = [node]
                while len(stack) > 0:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        if current == target:
                            return True
                        if current in self.graph:
                            for neighbor in self.graph[current]:
                                if neighbor not in visited:
                                        stack.append(neighbor)
        return False
    
    def topologicalSortHelper(self, node, visited, stack):
        visited[node] = True
        for nbr in self.graph[node]:
            if visited[nbr] == False:
                self.topologicalSortHelper(nbr,visited,stack) #recursively sort into stack each nbr to which node has a directed edge
        stack.append(node)
        
    def topologicalSort(self):
        stack = []
        visited = [False]*len(self.graph.keys()) #initialize each node as unvisited
        for node in self.graph.keys():
            if visited[node] == False: #if a node is already visited, it is already in our stack
                self.topologicalSortHelper(node, visited, stack)
        stack.reverse()
        return stack
                

        
        
    

my_graph = Graph([(5,0),(4,0),(4,1),(5,2),(2,3),(3,1)])
print(my_graph.graph)
print(my_graph.dfs(2))
print(my_graph.topologicalSort())
