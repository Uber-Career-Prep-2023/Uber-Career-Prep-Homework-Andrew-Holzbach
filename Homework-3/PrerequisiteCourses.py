"""
This is seemingly a topological sort question where the nodes are the classes, and directed edges point
from classes to classes that they are they are prerequisites for. The method should be to build a Adjacency
List graph representation and then run a topological sort so that no classes come before their prerequisites.

O(n+m) time complexity where n is the number of classes total and m is the number of prerequisites between classes
O(n) space complexity
Took 35 minutes
"""
#we can safely assume that the graph is acyclical because classes cannot be prequisites for other classes
#which are prerequisites for the original class 
def class_order(courses,prereqs):
    graph = prereqs
    for node in courses:
        if node not in prereqs:
            graph[node] = []
    # this creates the adj_list in graph
    stack = topo_sort(graph)
    return stack

def topo_sort(graph):
    stack = []
    visited = set()
    for node in graph:
        if node not in visited:
            topo_sort_helper(graph,stack,visited,node)
    return stack
    

def topo_sort_helper(graph, stack,visited,node):
    visited.add(node)
    for nbr in graph[node]:
        if nbr not in visited:
            topo_sort_helper(graph, stack,visited,nbr)
    stack.append(node)

print(class_order(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }))
print(class_order(["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
))