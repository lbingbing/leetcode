import random

char_set = [chr(ord('a')+i) for i in range(26)]

def gen(line_num):
    l = []
    cur_depth = 0
    for i in range(line_num):
        name = ''.join([random.choice(char_set) for i in range(random.randint(1,10))])
        ext = '.f' if random.randint(0,2)==0 else ''
        l.append(r'\t'*cur_depth+name+ext+r'\n')
        if cur_depth==0:
            cur_depth = random.randint(0,1)
        else:
            cur_depth = random.randint(cur_depth-1,cur_depth+1)
    return ''.join(l)

m = 200
n = 20

for m1 in range(m):
    n1 = random.randint(0,n)
    s = gen(n1)
    print('"'+s+'"')
