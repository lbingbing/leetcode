import random

def gen(n):
    l = [[i,n-i] for i in range(1,n+1)]
    return l

m = 1
f = open('log.txt','w')
for i in range(0,m):
    l = gen(1100)
    f.write(str(l).replace(' ','')+'\n')
f.close()
