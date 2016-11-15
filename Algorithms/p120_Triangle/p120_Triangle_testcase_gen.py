import random

k = 50
n = 10

for k1 in range(k):
    n1 = random.randint(1,n)
    #n1 = n
    l = [[random.randint(-20,20) for j in range(i)] for i in range(1,n1+1)]
    print(str(l).replace(' ',''))
