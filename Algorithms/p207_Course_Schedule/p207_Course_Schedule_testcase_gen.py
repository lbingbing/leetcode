import random

k = 100
n = 15

for k1 in range(k):
    n1 = random.randint(0,n)
    m1 = random.randint(0,n1*2)
    edges_s = set()
    edges_l = []
    for i in range(m1):
        while True:
            edge = (random.randint(0,n1-1),random.randint(0,n1-1))
            if edge in edges_s and random.randint(0,3)>0:
                continue
            if edge[0]==edge[1] and random.randint(0,6)>0:
                continue
            edges_s.add(edge)
            edges_l.append(list(edge))
            break
    print(n1)
    print(str(edges_l).replace(' ',''))
