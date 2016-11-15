import random

def gen(n):
    l = [random.randint(1,n//8*7) for i in range(0,n)]
    for i in range(n-1,-1,-1):
        num = 0
        for j in range(0,i):
            if l[j]>=l[i]:
                num += 1
        l[i] = [l[i],num]
    random.shuffle(l)
    return l

m = 1
f = open('log.txt','w')
for i in range(0,m):
    l = gen(100000)
    f.write(str(l).replace(' ','')+'\n')
f.close()
