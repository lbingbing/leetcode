import random

def gen(m, n):
    a = m*n*2
    l = [random.randint(1,a) for i in range(0,m*n)]
    l.sort()
    return [l[n*i:n*i+n] for i in range(0,m)]

k = 50
m = 20
n = 20

for i in range(0,k):
    m1 = random.randint(0,m)
    n1 = random.randint(0,n)
    a = m1*n1*2
    print(str(gen(m1,n1)).replace(' ',''))
    print(random.randint(0,a))
