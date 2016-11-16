import random

k = 2000
low = -30
high = 30

for k1 in range(k):
    x1,y1,x2,y2 = (random.randint(low,high) for i in range(4))
    if x1>x2:
        x1,x2 = x2,x1
    if y1>y2:
        y1,y2 = y2,y1
    print(x1)
    print(y1)
    print(x2)
    print(y2)
