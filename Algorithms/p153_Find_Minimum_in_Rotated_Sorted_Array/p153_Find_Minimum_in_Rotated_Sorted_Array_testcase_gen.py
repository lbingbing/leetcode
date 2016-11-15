import random

m = 50
n = 20

for i in range(0,m):
    l = random.sample(range(1,100),random.randint(1,n))
    l.sort()
    k = random.randint(0,len(l)-1)
    l = l[k:]+l[0:k]
    print(str(l).replace(' ',''))
