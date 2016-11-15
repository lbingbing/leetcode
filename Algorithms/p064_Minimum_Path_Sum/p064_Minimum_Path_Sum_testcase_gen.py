import random

k = 100
m = 20
n = 20
max_val = 20

for k1 in range(0,k):
    m1 = random.randint(1,m)
    n1 = random.randint(1,n)
    matrix = [[random.randint(0,max_val) for j in range(0,n1)] for i in range(0,m1)]
    print(str(matrix).replace(' ',''))
