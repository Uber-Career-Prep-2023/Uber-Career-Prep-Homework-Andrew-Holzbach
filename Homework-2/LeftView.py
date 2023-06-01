#took 35 minutes
#This seems like a bfs(level order left to right) since we need the leftmost on each level
#O(n) time complexity, O(n) space complexity

import binarysearchtree as bse

import queue

def left_view(tree):
    node_queue = queue.Queue()
    node_queue.put(tree)
    distance = {tree.data:0}
    current_level = 0 #this keeps track of the distance from the root, so we know when we move height
    return_array = [tree]
    while node_queue.qsize() > 0:
        current_node = node_queue.get()
        print(current_node.data)
        if distance[current_node.data] > current_level: #if the distance from the root is greater than the prior distance
            current_level += 1                          #we know this is the leftnmost node in it's level
            return_array.append(current_node.data)
        if current_node.left != None: #we want to search the leftmost nodes first, so put them in the queue first
            node_queue.put(current_node.left)
            distance[current_node.left.data] = distance[current_node.data] + 1
        if current_node.right != None:
            node_queue.put(current_node.right)
            distance[current_node.right.data] = distance[current_node.data] + 1
    return return_array

my_tree0 = bse.Node(7)
my_tree1 = bse.Node(8)
my_tree2 = bse.Node(3)
my_tree3 = bse.Node(9)
my_tree4 = bse.Node(13)
my_tree0.left = my_tree1
my_tree0.right = my_tree2
my_tree2.left = my_tree3
my_tree2.right = my_tree4        
print(left_view(my_tree0))