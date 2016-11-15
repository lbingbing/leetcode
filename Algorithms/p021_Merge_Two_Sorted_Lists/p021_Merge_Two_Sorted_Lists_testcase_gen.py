import random

m = 200
n = 30

for i in range(0,m):
    for j in range(0,2):
        l = [random.randint(1,n//2) for k in range(0,random.randint(0,n))]
        print(str(sorted(l)).replace(' ',''))
