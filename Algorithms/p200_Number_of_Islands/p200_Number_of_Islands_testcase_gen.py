import random

k = 200
m = 10
n = 10

for k1 in range(k):
    m1 = random.randint(0,m)
    n1 = random.randint(0,n)
    l = [[str(random.randint(0,1)) for j in range(n1)] for i in range(m1)]
    l = list(map(lambda x:''.join(x),l))
    print(str(l).replace(' ','').replace("'",'"'))
