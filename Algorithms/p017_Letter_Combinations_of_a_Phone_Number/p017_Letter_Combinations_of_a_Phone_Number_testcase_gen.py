import random

k = 50
n = 5

for k1 in range(k):
    n1 = random.randint(0,n)
    if random.randint(0,4)==0:
        l = [random.randint(0,9) for i in range(n1)]
    else:
        l = [random.randint(2,9) for i in range(n1)]
    print('"'+''.join(map(lambda x:str(x),l))+'"')
