import random

k = 200
n = 20

for k1 in range(k):
    while True:
        n1 = random.randint(0,n)
        n2 = random.randint(0,n)
        if n1+n2>0:
            break
    l1 = sorted([random.randint(0,n) for i in range(n1)])
    l2 = sorted([random.randint(0,n) for i in range(n2)])
    print(str(l1).replace(' ',''))
    print(str(l2).replace(' ',''))
