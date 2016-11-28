import random

k = 1000
n = 40

for k1 in range(k):
    n1 = random.randint(3,n)
    l = [random.randint(-n,n) for i in range(n1)]
    a = random.randint(-n*2,n*2)
    print(str(l).replace(' ',''))
    print(a)
