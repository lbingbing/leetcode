import gen_random_tree2

def serialize_inorder(tree):
    l = []
    inorder_traversal(tree,l)
    return l

def inorder_traversal(tree,l):
    if tree.nil:
        return
    inorder_traversal(tree.l,l)
    l.append(tree.val)
    inorder_traversal(tree.r,l)

def serialize_postorder(tree):
    l = []
    postorder_traversal(tree,l)
    return l

def postorder_traversal(tree,l):
    if tree.nil:
        return
    postorder_traversal(tree.l,l)
    postorder_traversal(tree.r,l)
    l.append(tree.val)

for i in range(0,100):
    tree = gen_random_tree2.number_tree(gen_random_tree2.gen_tree()) 
    l_inorder = serialize_inorder(tree)
    l_postorder = serialize_postorder(tree)
    print(str(l_inorder).replace(' ',''))
    print(str(l_postorder).replace(' ',''))

