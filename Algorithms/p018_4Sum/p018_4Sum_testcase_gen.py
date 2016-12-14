import random

k = 500
n = 40

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [random.randint(-n1,n1) for i in range(n1)]
    a = random.randint(-n1*4,n1*4)
    print(str(l).replace(' ',''))
    print(a)
