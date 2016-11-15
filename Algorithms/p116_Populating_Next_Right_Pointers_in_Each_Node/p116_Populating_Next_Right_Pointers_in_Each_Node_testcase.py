from collections import deque

def gen_tree(level):
    n = 2**level-1
    nodes = [TreeLinkNode(i) for i in range(1,n+1)]
    for i in range(0,n//2):
        nodes[i].left = nodes[i*2+1]
        nodes[i].right = nodes[i*2+2]
    return nodes[0] if nodes else None

def print_tree(tree):
    if not tree:
        return
    q = deque([tree]);
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

#s = Solution1()
s = Solution2()

for level in range(0,4):
    tree = gen_tree(level)
    print('level='+str(level))
    print('before:')
    print_tree(tree)
    s.connect(tree)
    print('after:')
    print_tree(tree)
    print()
