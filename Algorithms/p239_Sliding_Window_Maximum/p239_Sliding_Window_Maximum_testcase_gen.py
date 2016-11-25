import random

k = 200
n = 100

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [random.randint(-n,n) for i in range(n1)]
    a = random.randint(1,n1) if n1 else 0
    print(str(l).replace(' ',''))
    print(a)
