import random

k = 500
n = 15

cases = set()

for k1 in range(k):
    n1 = random.randint(1,n)
    l = sorted([random.randint(0,n1) for i in range(n1)])
    a = random.randint(-3,n1+2) if random.randint(0,1)==0 else random.choice(l)
    print(str(l).replace(' ',''))
    print(a)
