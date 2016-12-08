import random

k = 1000
n = 50

for k1 in range(k):
    n1 = random.randint(0,n)
    l = [chr(ord('a')+random.randint(0,25)) for i in range(n1)]
    print('"'+''.join(l)+'"')
