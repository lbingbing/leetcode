import random

k = 500
m = 10
n = 10


for k1 in range(0,k):
    m1 = random.randint(0,m)
    n1 = random.randint(0,n)
    #m1 = m
    #n1 = n
    matrix = [[random.randint(0,1) for j in range(0,n1)] for i in range(0,m1)]
    print(str(matrix).replace(' ',''))
