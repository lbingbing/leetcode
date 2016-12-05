import random

k = 200
n = 30

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [i for i in range(n1)]
    a = random.randint(0,n1+3)
    print(str(l).replace(' ',''))
    print(a)
