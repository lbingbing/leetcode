import random

def gen_char(error_injection):
    size = random.randint(1,4)
    l = [random.randint(0,255) for i in range(size)]
    if not error_injection or random.randint(0,9)<4:
        if size==1:
            l[0] &= 0x7f
        elif size==2:
            l[0] = (l[0]&0x1f)|0xc0
        elif size==3:
            l[0] = (l[0]&0xf)|0xe0
        elif size==4:
            l[0] = (l[0]&0x7)|0xf0
        for i in range(1,size):
            l[i] = (l[i]&0x3f)|0x80
    return l

m = 500
n = 10

for m1 in range(0,m):
    n1 = random.randint(0,n)
    l = []
    for i in range(n1):
        l += gen_char(1)
    print(str(l).replace(' ',''))
