import random

k = 500
n = 50

for k1 in range(k):
    n1 = random.randint(1,n)
    set1 = [0]*n1+list(range(1,n1))
    l = [random.choice(set1) for i in range(n1)]
    print(str(l).replace(' ',''))
