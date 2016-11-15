import random
import math

def fn():
    l = [0,1]
    for i in range(4,40):
        l.append(l[-1]+random.randint(int(math.sqrt(i))//2,int(math.sqrt(i))))
    return l

for i in range(0,100):
    print(str(fn()).replace(' ',''))
