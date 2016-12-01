import random

k = 1000
n1 = 50
n2 = 50

set1 = [chr(ord('a')+i) for i in range(26)]

for k1 in range(k):
    n11 = random.randint(0,n1)
    n21 = random.randint(0,n2)
    set2 = random.sample(set1,random.randint(1,26))
    s1 = ''.join(random.choice(set2) for i in range(n11))
    s2 = ''.join(random.choice(set2) for i in range(n21))
    print('"'+s1+'"')
    print('"'+s2+'"')
