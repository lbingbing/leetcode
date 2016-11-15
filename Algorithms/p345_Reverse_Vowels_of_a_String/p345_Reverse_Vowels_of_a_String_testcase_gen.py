import random

m = 200
n = 100

char_set = [chr(ord('a')+i) for i in range(0,26)]
char_set += [chr(ord('A')+i) for i in range(0,26)]

for i in range(0,m):
    l = [random.choice(char_set) for j in range(0,random.randint(0,n))]
    print('"'+''.join(l)+'"')
