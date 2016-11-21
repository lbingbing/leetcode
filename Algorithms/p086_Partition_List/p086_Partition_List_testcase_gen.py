import random

k = 200
n = 10

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [random.randint(0,n1) for i in range(n1)]
    a = random.randint(-int(n1/4),int(n1*5/4))
    print(str(l).replace(' ',''))
    print(a)
