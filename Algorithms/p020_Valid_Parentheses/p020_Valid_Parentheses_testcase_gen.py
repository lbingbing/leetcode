import random

k = 200
n = 10

for k1 in range(k):
    n1 = random.randint(0,n)
    num = [None]*3
    num[0] = random.randint(0,n1)
    num[1] = random.randint(0,n1-num[0])
    num[2] = n1-num[0]-num[1]
    choices = ''
    if num[0]>0:
        choices += '('
    if num[1]>0:
        choices += '['
    if num[2]>0:
        choices += '{'
    l = []
    while choices:
        c = random.choice(choices)
        l.append(c)
        if c=='(':
            choices = choices.replace(c,')')
        elif c=='[':
            choices = choices.replace(c,']')
        elif c=='{':
            choices = choices.replace(c,'}')
        elif c==')':
            num[0] -= 1
            choices = choices.replace(c,'(' if num[0]>0 else '')
        elif c==']':
            num[1] -= 1
            choices = choices.replace(c,'[' if num[1]>0 else '')
        elif c=='}':
            num[2] -= 1
            choices = choices.replace(c,'{' if num[2]>0 else '')
    if l and random.randint(0,2)==0:
        l.pop(random.randint(0,len(l)-1))
    print('"'+''.join(l)+'"')
