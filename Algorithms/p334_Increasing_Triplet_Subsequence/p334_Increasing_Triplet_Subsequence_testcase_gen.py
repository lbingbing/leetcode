import random

m = 500
n = 7
for i in range(0,m):
    l = [random.randint(1,n*2) for j in range(0,n)]
    print(str(l).replace(' ',''))
