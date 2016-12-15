import random

k = 100
m = 10
n = 10

for k1 in range(k):
    l = [sorted(random.randint(0,m*n) for j in range(random.randint(0,n)))
         for i in range(random.randint(0,m))]
    print(str(l).replace(' ',''))
