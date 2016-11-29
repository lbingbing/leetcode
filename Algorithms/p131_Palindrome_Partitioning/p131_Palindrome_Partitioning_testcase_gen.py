import random

k = 100
n = 15

for k1 in range(k):
    l = [random.choice('abcde') for i in range(random.randint(0,n))]
    print('"'+''.join(l)+'"')
