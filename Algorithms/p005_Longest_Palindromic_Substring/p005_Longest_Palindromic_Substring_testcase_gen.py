import random

k = 200
n = 100
set1 = 'abcdef'

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [random.choice(set1) for i in range(n1)]
    print('"'+''.join(l)+'"')
