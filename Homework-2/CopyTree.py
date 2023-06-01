#took 20 minutes
#pre-order traversal recursion
#O(n) time complexity O(n) space complexity 
import binarysearchtree as bse

def copytreerecursive(tree):
    """
    input: tree - a binary search tree 

    output: root, the root of a deep copy of the binary search tree
    """
    root = bse.Node(tree.data)
    root.right = copytreehelper(tree.right)
    root.left = copytreehelper(tree.left)
    return root

def copytreehelper(tree):
    """
    input: tree - a binary search tree

    output: none

    creates a deep copy of the binary search tree by copying the root node and
    then recursively copying the left and right subtrees
    """
    if tree == None:
        return None
    else:
        root = bse.Node(tree.data)
        root.right = copytreehelper(tree.right)
        root.left = copytreehelper(tree.left)

"""
tree = bse.Node(10)
tree.insert(5)
tree.insert(11)
tree.insert(3)
tree.insert(13)
tree.insert(2)
print(tree.data)
print(tree.max())
print(tree.min())
tree_copy = copytreerecursive(tree)
print(tree.data)
print(tree.max())
print(tree.min())
"""