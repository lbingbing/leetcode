import random

m = 10
len_factor = 7

def gen(level,val):
    up = int(len_factor/(level**0.5))
    l = [random.randint(0,up) for i in range(0,random.randint(1,up+1))]
    for i in range(0,len(l)):
        if l[i]==0:
            val[0] += 1
            l[i] = val[0]
        else:
            l[i] = gen(level+1,val)
    return l

for m1 in range(0,m):
    val = [0]
    print(str(gen(1,val)).replace(' ',''))
