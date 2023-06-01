#took 20 minutes
#pre-order traversal recursion
#O(n) time complexity O(log(n)) space complexity 
import binarysearchtree as bse

def is_bst_rec(tree):
    if tree.right == None and tree.left == None:
        return True
    elif tree.left == None and tree.right.data > tree.data:
        return is_bst_rec(tree.right)
    elif tree.right == None and tree.left.data < tree.data:
        return is_bst_rec(tree.left)
    elif tree.right.data > tree.data and tree.left.data < tree.data:
        return is_bst_rec(tree.right) and is_bst_rec(tree.left)
    else:
        return False

my_tree = bse.Node(10)
my_tree.insert(8)
my_tree.insert(16)
my_tree.insert(9)
my_tree.insert(13)
print(is_bst_rec(my_tree))
node0 = bse.Node(5)
node1 = bse.Node(4)
node2 = bse.Node(3)
node0.left = node1
node1.right = node2
print(is_bst_rec(node0))