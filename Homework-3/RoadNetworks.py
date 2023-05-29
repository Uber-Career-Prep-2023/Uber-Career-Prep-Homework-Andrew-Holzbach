import queue as que
"""
We can reason about the cities as nodes, and roads between them as undirected edges.
We want to find the number of unconnected components of our graph that include at least one road/edge,
we can do this by employing bfs from various start nodes until each node has been visited, and counting the
times we see a component containing at least one edge
 
O(n + m) n number of nodes, m number of edges
took 40 minutes
"""
def conv_adj_list(nodes, edges):
    """
    Converts input towns as nodes and roads as edges into adjacency list form
    """
    adj_list = {}
    for node in nodes:
        adj_list[node] = []
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    return adj_list
    


def road_networks(towns, roads):
    if len(towns) == 0 or len(towns) == 1 or len(roads) == 0:
        return 0
    graph = conv_adj_list(towns, roads)
    network_num = 0
    visited = set()
    for cur_town in towns:
        if cur_town not in visited:
            print(cur_town)
            visited.add(cur_town)
            if len(graph[cur_town]) > 0: #we want to check that cur_town is the member of a road network
                network_num += 1 #then we will increment up because we are going to use bfs to add all members of this network to visited
            queue = que.Queue()
            queue.put(cur_town)
            while queue.qsize() != 0:
                cur_node = queue.get()
                for nbr in graph[cur_node]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.put(nbr)
    return network_num


num1 = road_networks(["a","b","c"], [("a","b"),("b","c")])
num2 = road_networks(["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"], [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")])
print(num1)
print(num2)