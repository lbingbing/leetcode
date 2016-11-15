import random
import collections

m = 100000

stack1 = Stack()
stack2 = []

for m1 in range(0,m):
    if stack1.empty()!=(not stack2):
        print('incorrect')
        break
    if not stack1.empty():
        if stack1.top()!=stack2[-1]:
            print('incorrect')
            break
    if stack1.empty() or random.randint(0,3)<2:
        v = random.randint(0,100)
        stack1.push(v)
        stack2.append(v)
    else:
        stack1.pop()
        stack2.pop()
