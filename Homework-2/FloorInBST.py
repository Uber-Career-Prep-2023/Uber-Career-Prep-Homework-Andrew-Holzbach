#took 27 minutes
#In-Order traversal recursive
#O(n) time complexity, and O(log(n)) space complexity
import binarysearchtree as bse

def floor_bst(tree, value):
    print(tree.data)
    if tree.data == value:
        return value
    elif tree.data > value:
        if tree.left != None:
            return floor_bst(tree.left, value)
        else:
            return None
    else: #when tree.data < value:
        if tree.right == None:
            return tree.data
        right_tree_floor = floor_bst(tree.right, value)
        if tree.data < right_tree_floor and right_tree_floor <= value:
            return right_tree_floor
        else:
            return tree.data

"""
my_bse = bse.Node(10)
my_bse.insert(8)
my_bse.insert(16)
my_bse.insert(9)
my_bse.insert(13)
my_bse.insert(17)
my_bse.insert(20)
print(floor_bst(my_bse,13))
"""