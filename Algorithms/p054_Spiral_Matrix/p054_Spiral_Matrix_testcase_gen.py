def gen(m, n):
    return [[i*n+j+1 for j in range(0,n)] for i in range(0,m)]

m = 10
n = 10

for i in range(0,m):
    for j in range(0,n):
        print(str(gen(i,j)).replace(' ',''))
