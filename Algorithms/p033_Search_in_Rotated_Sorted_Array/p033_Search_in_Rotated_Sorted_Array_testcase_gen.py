import random

k = 500
n = 20

for k1 in range(k):
    n1 = random.randint(1,n)
    l = sorted(random.sample(range(n),n1))
    pos = random.randint(0,n1-1)
    a = l[pos]
    if n1>1 and random.randint(0,1)==0:
        l.pop(pos)
    rotate_left = random.randint(0,n1-1)
    l = l[rotate_left:]+l[0:rotate_left]
    print(str(l).replace(' ',''))
    print(a)
