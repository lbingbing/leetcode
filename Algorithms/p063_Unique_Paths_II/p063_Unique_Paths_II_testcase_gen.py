import random

k = 200
m = 10
n = 10

for k1 in range(k):
    m1 = random.randint(1,m)
    n1 = random.randint(1,n)
    choices = lambda i,j: (0,)*(abs(i+j-(m+n-2))+2)+(1,)
    matrix = [[random.choice(choices(i,j)) for j in range(n1)] for i in range(m1)]
    print(str(matrix).replace(' ',''))
