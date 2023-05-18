
def is_bst_rec(tree):
    if tree.right == None and tree.left == None:
        return True
    elif tree.right.data > tree.data and tree.left.data < tree.data:
        return is_bst_rec(tree.right) and is_bst_rec(tree.left)
    
    else:
        return False