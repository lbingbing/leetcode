import random

k = 100
n = 50

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [random.randint(-n,n) for i in range(n1)]
    print(str(l).replace(' ',''))
