import random

k = 100
m = 20
n = 20

for k1 in range(k):
    m1 = random.randint(0,m)
    n1 = random.randint(0,n)
    l1 = sorted([random.randint(-m,m) for i in range(m1)])
    l2 = sorted([random.randint(-n,n) for i in range(n1)])
    a = random.randint(0,m1*n1)
    print(str(l1).replace(' ',''))
    print(str(l2).replace(' ',''))
    print(a)
