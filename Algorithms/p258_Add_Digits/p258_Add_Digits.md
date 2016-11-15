Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

A naive implementation of the above process is trivial. Could you come up with other methods?
What are all the possible results?
How do they occur, periodically or randomly?
You may find this Wikipedia article useful.
https://en.wikipedia.org/wiki/Digital_root

solution:

f(n): recursive reduction addition
g(n): one step of reduction addition
h(n): num of carries performed for n+1

then
f(n)=f(g(n))
g(n+1)=g(n)-9h(n)+1

because
g(n)=g(n-1)-9h(n-1)+1
g(n-1)=g(n-2)-9h(n-2)+1
...
g(2)=g(1)-9h(1)+1
g(1)=1

then
g(n)=n-9(h(1)+h(2)+...+h(n-1))

base on observation of f(n), assume
f(i)=(i-1)%9+1 // for i=1,2,...,k
then
f(k+1)
=f(g(k+1))
=f(g(k)-9h(k)+1)
=(g(k)-9h(k)+1-1)%9+1 // g(k)-9h(k)+1 << k for a large k
=g(k)%9+1
=k%9+1
=(k+1-1)%9+1

then
f(n)=(n-1)%9+1