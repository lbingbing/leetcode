import random

m = 20
n = 10

for m1 in range(0,m):
    l = [random.randint(0,n) for n1 in range(0,random.randint(0,n))]
    print(str(l).replace(' ',''))
