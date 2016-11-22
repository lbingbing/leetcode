import random
import math

k = 200
n = 100

for k1 in range(k):
    n1 = random.randint(0,int(math.log2(n))*2)
    l = sorted([random.randint(0,n) for i in range(n1)])
    a = random.randint(0,n*2);
    print(str(l).replace(' ',''))
    print(a)
