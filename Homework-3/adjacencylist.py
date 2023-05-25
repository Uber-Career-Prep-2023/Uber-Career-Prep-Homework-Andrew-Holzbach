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
        for node in self.graph.keys():
            if node not in visited:
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
                self.topologicalSortHelper(nbr,visited,stack)
        stack.append(node)
        
    def topologicalSort(self):
        stack = []
        visited = [False]*len(self.graph.keys())
        for node in self.graph.keys():
            if visited[node] == False:
                self.topologicalSortHelper(node, visited, stack)
        stack.reverse()
        return stack
                

        
        
    

my_graph = Graph([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)])
print(my_graph.graph)
print(my_graph.dfs(2))
print(my_graph.topologicalSort())