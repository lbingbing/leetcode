import random

k = 1000
n = 100
m = 5

char_set = [chr(ord('a')+i) for i in range(0,26)]

for k1 in range(k):
    n1 = random.randint(0,n)
    m1 = random.randint(1,m)
    s1 = ''.join([random.choice(char_set) for i in range(n1)])
    s2 = ''.join([random.choice(char_set) for i in range(m1)])
    print('"'+s1+'"')
    print('"'+s2+'"')
