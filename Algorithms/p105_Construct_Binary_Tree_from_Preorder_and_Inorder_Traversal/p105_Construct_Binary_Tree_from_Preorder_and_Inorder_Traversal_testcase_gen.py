import gen_random_tree2

def serialize_preorder(tree):
    l = []
    preorder_traversal(tree,l)
    return l

def preorder_traversal(tree,l):
    if tree.nil:
        return
    l.append(tree.val)
    preorder_traversal(tree.l,l)
    preorder_traversal(tree.r,l)

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

for i in range(0,100):
    tree = gen_random_tree2.number_tree(gen_random_tree2.gen_tree()) 
    l_preorder = serialize_preorder(tree)
    l_inorder = serialize_inorder(tree)
    print(str(l_preorder).replace(' ',''))
    print(str(l_inorder).replace(' ',''))

