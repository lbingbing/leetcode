import random

n = 10
level = 4
choices1 = [1]*80
choices1 += [0]*20
choices2 = [1]*50
choices2 += [0]*50

def gen():
    l = [1]
    last_level_state = [1]
    for i in range(0,level):
        cur_level_state = []
        for node in last_level_state:
            if node:
                cur_level_state += [random.choice(choices1)]
                cur_level_state += [random.choice(choices2)]
        if any(cur_level_state):
            l += cur_level_state
            last_level_state = cur_level_state
        else:
            break
    
    end = len(l) - list(reversed(l)).index(1) - 1
    l = l[0:end+1]
    
    l = map(lambda x: '1' if x else 'null',l)
    print('[',end='')
    print(','.join(l),end='')
    print(']')

for i in range(0,n):
    gen()
