import random
import gen_random_tree2

def number_tree(tree):
    if tree and not tree.nil:
        tree.val = random.randint(0,9)
        number_tree(tree.l)
        number_tree(tree.r)
    return tree

m = 200

for i in range(0,m):
        l = gen_random_tree2.serialize_tree(number_tree(gen_random_tree2.gen_tree()))
        print('['+','.join(l)+']')
