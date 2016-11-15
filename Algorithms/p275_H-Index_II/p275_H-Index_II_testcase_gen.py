import random

m = 500
n = 50

for m1 in range(m):
    n1 = random.randint(0,n)
    l = [random.randint(0,n1) for i in range(n1)]
    l.sort()
    print(str(l).replace(' ',''))
