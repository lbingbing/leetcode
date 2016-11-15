import random

for i in range(0,200):
    l = [random.randint(-10,10) for j in range(0,random.randint(1,31))]
    print(str(l).replace(' ',''))
