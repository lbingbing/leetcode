import random

k = 100
n = 30

for k1 in range(k):
    n1 = random.randint(0,n)
    l1 = ''.join([str(random.randint(0,9)) for i in range(n1)])
    l2 = ''.join([str(random.randint(0,9)) for i in range(n1)])
    print('"'+l1+'"')
    print('"'+l2+'"')
