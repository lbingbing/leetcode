import random

m = 100
n = 100

for m1 in range(0,m):
    n1 = random.randint(1,n)
    l = [random.randint(0,n1) for i in range(0,n1)]
    print(str(l).replace(' ',''))
    print(random.randint(1,n1))
