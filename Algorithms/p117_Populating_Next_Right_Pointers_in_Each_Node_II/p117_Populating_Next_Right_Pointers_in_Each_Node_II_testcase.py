from collections import deque

import gen_random_tree2

def gen_tree():
    return localize_tree(gen_random_tree2.number_tree(gen_random_tree2.gen_tree()))

def localize_tree(tree):
    if not tree or tree.nil:
        return None
    tree1 = TreeLinkNode(tree.val)
    tree1.left = localize_tree(tree.l);
    tree1.right = localize_tree(tree.r);
    return tree1

def copy_tree(tree):
    if not tree:
        return None
    tree1 = TreeLinkNode(tree.val)
    tree1.left = copy_tree(tree.left);
    tree1.right = copy_tree(tree.right);
    return tree1

def compare_tree(tree1, tree2):
    if not tree1 and not tree2:
        return True
    elif tree1 and tree2:
        if tree1.val!=tree2.val:
            return False
        if not ((not tree1.next and not tree2.next) or
                (tree1.next and tree2.next and tree1.next.val==tree2.next.val)):
            return False
        if not (compare_tree(tree1.left,tree2.left) and compare_tree(tree1.right,tree2.right)):
            return False
        return True
    else:
        return False

def print_tree(tree):
    if not tree:
        return
    q = deque([tree])
    while q:
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        print('s:',node.val,end=', ')
        print('l:',node.left.val if node.left else 'null',end=', ')
        print('r:',node.right.val if node.right else 'null',end=', ')
        print('n:',node.next.val if node.next else 'null')

class Solution2:
    def connect(self, root):
        if not root:
            return None
        q = deque([root])
        while q:
            size = len(q)
            for i in range(0,size-1):
                q[i].next = q[i+1]
            for i in range(0,size):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                q.popleft()

s1 = Solution1()
s2 = Solution2()

for level in range(0,10000):
    tree1 = gen_tree()
    tree2 = copy_tree(tree1)
    #print('before:')
    #print('tree1')
    #print_tree(tree1)
    #print('tree2')
    #print_tree(tree2)
    s1.connect(tree1)
    s2.connect(tree2)
    if not compare_tree(tree1,tree2):
        print('mismatched')
    #print('after:')
    #print('tree1')
    #print_tree(tree1)
    #print('tree2')
    #print_tree(tree2)
    #print()
