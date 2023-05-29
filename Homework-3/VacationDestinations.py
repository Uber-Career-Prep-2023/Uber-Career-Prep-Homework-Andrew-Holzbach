"""
This seems like a modified bfs problem
Took 23 minutes
O(n + m) Time complexity
O(n + m) Space complexity
"""
import queue

def vac_dest(origin, k, edges):
    if len(edges) == 0:
        return 0, []
    graph = {}
    for edge in edges:
        graph[edge[0]] = []
        graph[edge[1]] = []
    for edge in edges:
        graph[edge[0]].append((edge[1],edge[2]))
        graph[edge[1]].append((edge[0],edge[2])) # initialize the adj_lst
    distance_reachable = {origin:0}
    mqueue = queue.Queue()
    mqueue.put(origin)
    while mqueue.qsize() > 0:
        node = mqueue.get()
        for nbr in graph[node]:
            if distance_reachable[node] + nbr[1] <= k: #this checks that nbr is still reachable under distance k
                distance_reachable[nbr[0]] = distance_reachable[node] + nbr[1] + 1 #we add one to account for the waiting time
                mqueue.put(nbr[0])
    distance_reachable.pop(origin)
    return len(distance_reachable), distance_reachable.keys()
        
#print(vac_dest('New York', 5,[("Boston", "New York", 4), ("New York", "Philadelphia.", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]))
print(vac_dest('New York', 8,[("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]
))