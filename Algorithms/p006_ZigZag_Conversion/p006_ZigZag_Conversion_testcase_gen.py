import random

k = 200
n = 50
rows = 50
set1 = [chr(ord('a')+i) for i in range(26)]

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [random.choice(set1) for i in range(n1)]
    rows1 = random.randint(0,rows)
    print('"'+''.join(l)+'"')
    print(rows1)
