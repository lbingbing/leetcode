import random

k = 500
n = 10

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [[random.randint(1,n),random.randint(1,n)] for i in range(n1)]
    print(str(l).replace(' ',''))
