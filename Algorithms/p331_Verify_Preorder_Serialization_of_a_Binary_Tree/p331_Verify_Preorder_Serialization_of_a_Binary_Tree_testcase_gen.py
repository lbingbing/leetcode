import random

m = 2000
len_set = [1,3,5,7,9,11]

for m1 in range(m):
    n1 = random.choice(len_set)
    l = []
    for i in range(n1):
        if random.randint(0,4)==0:
            l.append('#')
        else:
            l.append(str(random.randint(0,19)))
    if len(l)==1 and l[0]=='#':
        continue
    print('"'+','.join(l)+'"')
