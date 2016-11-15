import random

k = 100
m = 5
n = 5

for k1 in range(k):
    #m1 = random.randint(1,m)
    #n1 = random.randint(1,n)
    m1 = m
    n1 = n
    l = [[random.randint(1,m*n) for j in range(n1)] for i in range(m1)]
    print(str(l).replace(' ',''))
