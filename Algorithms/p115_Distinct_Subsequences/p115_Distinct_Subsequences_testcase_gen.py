import random

k = 500
n = 20

set1 = [chr(ord('a')+i) for i in range(26)]

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [random.choice(set1) for i in range(n1)]
    t = ''.join(l)
    n2 = random.randint(0,n*4)
    for i in range(n2):
        l.insert(random.randint(0,len(l)),random.choice(set1))
    s = ''.join(l)
    print('"'+s+'"')
    print('"'+t+'"')
