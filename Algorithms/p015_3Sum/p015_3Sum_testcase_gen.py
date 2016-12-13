import random

k = 200
n = 30

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [random.randint(-n1,n1) for i in range(n1)]
    print(str(l).replace(' ',''))
