import random
from collections import deque

n = 100
choices = [[True]*30 + [False]*50,
           [True]*40 + [False]*20,
           [True]*50 + [False]*10,]
speed = 3

class TreeNode:
    def __init__(self, nil = False):
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

def serialize_tree(tree):
    q = deque([tree])
    l = []
    while q:
        node = q.popleft()
        if not node.nil:
            l.append(True)
        else:
            l.append(False)
        if node.l:
            q.append(node.l)
        if node.r:
            q.append(node.r)
    return l

for i in range(0,n):
    l1 = serialize_tree(gen_tree())
    end = len(l1) - list(reversed(l1)).index(True) - 1
    l1 = l1[0:end+1]
    l2 = []
    i = 1
    for b in l1:
        if b:
            l2.append(str(i))
            i += 1
        else:
            l2.append('null')
    print('[',end='')
    print(','.join(l2),end='')
    print(']')
