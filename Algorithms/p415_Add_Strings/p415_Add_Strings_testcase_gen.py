import random

m = 20
n = 5100

char_set = [chr(ord('0')+i) for i in range(0,10)]

for i in range(0,m):
    for j in range(0,2):
        l = [random.choice(char_set) for k in range(0,n)]
        print('"'+''.join(l)+'"')
