import random
from collections import deque

m = 100000

q1 = Queue()
q2 = deque()

for m1 in range(0,m):
    if q1.empty()!=(not q2):
        print('incorrect')
        break
    if q1.empty() or random.randint(0,3)<2:
        v = random.randint(0,100)
        q1.push(v)
        q2.append(v)
    else:
        if q1.peek()!=q2[0]:
            print('incorrect')
            break
        q1.pop()
        q2.popleft()
