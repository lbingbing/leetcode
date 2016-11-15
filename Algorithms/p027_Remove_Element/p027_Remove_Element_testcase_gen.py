import random

m = 1000
n = 10

for m1 in range(0,m):
    n1 = random.randint(0,n)
    l = [random.randint(0,4) for i in range(0,n1)]
    val = random.randint(0,4)
    print(str(l).replace(' ',''))
    print(val)
