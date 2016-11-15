import random

k = 50
m = 50
n = 50
max_val = 100

for k1 in range(k):
    #m1 = random.randint(0,m)
    #n1 = random.randint(0,n)
    m1 = m
    n1 = n
    l = [[random.randint(0,max_val) for j in range(n1)] for i in range(m1)]
    print(str(l).replace(' ',''))
