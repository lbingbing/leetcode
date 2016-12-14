import random

k = 1000
n = 50

for k1 in range(k):
    n11 = random.randint(0,5)
    n12 = random.randint(0,1)
    n13 = random.randint(0,n-n11-n12)
    set1 = ' '
    set2 = '+---'
    set3 = ' +-'*1+'abc'*1+'0123456789'*random.randint(1,6)
    l = [random.choice(set1)*n11]
    l += [random.choice(set2) for i in range(n12)]
    l += [random.choice(set3) for i in range(n13)]
    print('"'+''.join(l)+'"')
