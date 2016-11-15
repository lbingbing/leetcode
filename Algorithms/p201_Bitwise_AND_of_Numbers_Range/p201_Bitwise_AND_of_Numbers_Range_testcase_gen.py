import random

k = 1000
for k1 in range(k):
    m = random.randint(0,0x7fffffff)
    n = random.randint(0,0x7fffffff)
    m,n = min(m,n),max(m,n)
    print(m)
    print(n)
