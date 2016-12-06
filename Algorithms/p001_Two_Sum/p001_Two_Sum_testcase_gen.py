import random

k = 200
m = 50
n = 20
s = set(i for i in range(0,m))

for k1 in range(k):
    n1 = random.randint(0,n)
    t = random.randint(0,m*2-1)
    s1 = set(s)
    l = []
    v1 = random.randint(0,t)
    v2 = t-v1
    l.append(v1)
    l.append(v2)
    s1.discard(v1)
    s1.discard(v2)
    while n1>0:
        v1 = random.choice(list(s1))
        v2 = t-v1
        l.append(v1)
        s1.discard(v2)
        n1 -= 1
    random.shuffle(l)
    print(str(l).replace(' ',''))
    print(t)
