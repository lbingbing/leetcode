import random

def gen(n):
    #l = [random.randint(1,int(n/8*7)) for i in range(0,n)]
    l = random.sample(range(1,n+1),n)
    for i in range(n-1,-1,-1):
        num = 0
        for j in range(0,i):
            if l[j]>=l[i]:
                num += 1
        l[i] = [l[i],num]
    l = list(enumerate(l,0))
    l.sort(key=lambda x:x[1][0])
    l = list(enumerate(l,1))
    l.sort(key=lambda x:x[1][0])
    l = list(map(lambda x:[x[0],x[1][1][0],x[1][1][1]],l))
    return l

n = 4
m = 1
f = open('log.txt','w')
for i in range(0,m):
    l = gen(n)
    f.write(str(l).replace(' ','')+'\n')
    for j in range(1,n):
        if l[j][0]+l[j][2]<l[j-1][0]+l[j-1][2]:
            f.write(str(j-1)+','+str(j)+'\n')
f.close()
