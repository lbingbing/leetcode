import random
import math

k = 10
n = 20
m = 20

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [random.randint(0,m) for i in range(0,n1)]
    a = random.randint(min(l)-1,sum(l)+1) if l else 0
    print(str(l).replace(' ',''))
    print(a)
