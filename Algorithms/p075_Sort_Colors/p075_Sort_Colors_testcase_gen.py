import random

m = 200
n = 50

for m1 in range(0,m):
    l = [random.randint(0,2) for i in range(0,random.randint(0,n))]
    print(str(l).replace(' ',''))
