import random

k = 1000
n = 20

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [random.randint(0,int(n1**1.5)) for i in range(n1)]
    a = random.randint(0,n1)
    b = random.randint(0,3)
    print(str(l).replace(' ',''))
    print(a)
    print(b)
