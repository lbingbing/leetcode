import random

k = 100
n = 20

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [random.randint(0,n1) for i in range(n1)]
    print(str(l).replace(' ',''))
