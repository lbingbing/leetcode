import random

def gen(m, n):
    a = m*n
    matrix = [[random.randint(1,a) for j in range(0,n)] for i in range(0,m)]
    #print_m(matrix)
    for k in range(m-1,-1,-1):
        i = k
        j = n-1
        while i<=m-1 and j>=0:
            maintain_property(matrix,i,j)
            i += 1
            j -= 1
    for k in range(n-2,-1,-1):
        i = 0
        j = k
        while i<=m-1 and j>=0:
            maintain_property(matrix,i,j)
            i += 1
            j -= 1
    return matrix

def maintain_property(matrix, i, j):
    #print(i,j)
    if j<len(matrix[0])-1 and matrix[i][j+1]<matrix[i][j] and (i>=len(matrix)-1 or matrix[i][j+1]<=matrix[i+1][j]):
        matrix[i][j+1],matrix[i][j] = matrix[i][j],matrix[i][j+1] 
        #print_m(matrix)
        maintain_property(matrix,i,j+1)
    elif i<len(matrix)-1 and matrix[i+1][j]<matrix[i][j] and (j>=len(matrix[0])-1 or matrix[i+1][j]<=matrix[i][j+1]):
        matrix[i+1][j],matrix[i][j] = matrix[i][j],matrix[i+1][j] 
        #print_m(matrix)
        maintain_property(matrix,i+1,j)

def print_m(matrix):
    for e in matrix:
        print(e)
    print()

k = 200
m = 10
n = 10

for i in range(0,k):
    m1 = random.randint(1,m)
    n1 = random.randint(1,n)
    #m1 = m
    #n1 = n
    a = int(m1*n1*1.2)
    matrix = gen(m1,n1)
    #print('final')
    #print_m(matrix)
    print(str(matrix).replace(' ',''))
    print(random.randint(0,a))
