import random
from collections import deque

choices = [[True]*7 + [False]*1,
           [True]*8 + [False]*1,
           [True]*9 + [False]*1,]
speed = 2

class TreeNode:
    def __init__(self, nil = False):
        self.val = None
        self.nil = nil
        self.l = None
        self.r = None

def gen_tree():
    tree = TreeNode(False)
    grow_tree(tree,2)
    return tree

def grow_tree(node, level):
    l_choice = random.choice(choices)
    r_choice = random.choice(choices)
    l = random.choice(l_choice+[False]*level*speed)
    r = random.choice(r_choice+[False]*level*speed)
    node.l = TreeNode(not l)
    node.r = TreeNode(not r)
    if l:
        grow_tree(node.l, level+1)
    if r:
        grow_tree(node.r, level+1)

def number_tree(tree):
    val = 0
    def number_tree_helper(tree):
        nonlocal val
        if tree and not tree.nil:
            number_tree_helper(tree.l)
            val += 1
            tree.val = val
            number_tree_helper(tree.r)
    number_tree_helper(tree)
    return tree

def serialize_tree(tree):
    q = deque([tree])
    l = []
    while q:
        node = q.popleft()
        if not node.nil:
            l.append(str(node.val))
        else:
            l.append('null')
        if node.l:
            q.append(node.l)
        if node.r:
            q.append(node.r)
    while l and l[-1]=='null':
        l.pop()
    return l

if __name__ == "__main__":
    m = 20
    for i in range(0,m):
        l = serialize_tree(number_tree(gen_tree()))
        print('['+','.join(l)+']')
