"""
We could create an adjacency_list mapping where each node maps to two separate lists of nodes, one for blue 
edges and one for red edges. For example {a:([b],[c])} means the graph consists of a-->b(red) and a-->c(blue)
we could then use an "alternating" bfs to check. 

Didn't finish in 40 minutes :()
"""
import queue

def convert_adj_list(edges):
    adj_list = {}
    for edge in edges:
        if edge[0] not in adj_list:
            adj_list[edge[0]] = ([],[])
        if edge[1] not in adj_list:
            adj_list[edge[1]] = ([],[])
    for edge in edges:
        if edge[2] == "red":
            adj_list[edge[0]][0].append(edge[1])
        if edge[2] == "blue":
            adj_list[edge[0]][1].append(edge[1])
    return adj_list
            

def alternating_path(edges, origin, destination):
    graph = convert_adj_list(edges)
    distance = {(origin,0):0,(origin,1):0} # 0 represents red, 1 represents blue
    colored_queue = queue.Queue()
    colored_queue.put((origin,0))
    colored_queue.put((origin,1)) # the color after the ordered pair represents the color of the edges that can leave this node
    dist_from_origin = 0
    while colored_queue.qsize() > 0:
        info = colored_queue.get()
        distance[info] = dist_from_origin
        node = info[0]
        next_color = info[1]
        for nbr in 
        dist_from_origin += 1
        
print(convert_adj_list([('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")]))