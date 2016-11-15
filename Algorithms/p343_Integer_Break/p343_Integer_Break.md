Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

Hint:

There is a simple O(n) solution to this problem.
You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

solution 1:
f(n): the answer
g(n): max(n,f(n))

f(n)=max(
1*g(n-1),
2*g(n-2),
...
(n-2)*g(2),
(n-1)*g(1)
)

g(n)=max(n,f(n))
g(1)=1


solution 2:
for k-partitioning case:
n=a1+a2+...+ak
then
a1a2...ak=(n-a2-a3-...-ak)a2a3...ak

for any given a3,a4,...,ak
a1a2...ak gets the max value when a2=(n-a3-a4-...-ak)/2
similarly,
for any given a2,a4,...,ak
a3=(n-a2-a4-...-ak)/2, a1a2...ak gets the max value
...

so when a1=a2=...=ak=n/k, (a1a2...ak)max=(n/k)^k

for g(k)=(n/k)^k, k=n/e, g(k) gets the max value
g(n/2)=2^(n/2)=e^((nln2/2)
g(n/3)=3^(n/3)=e^((nln3/3)
g(n/3)>g(n/2)

so divide n into 3's if possible to get f(n)
n=3k => 3*3*...*3
n=3k+1 => 3*3*..*3*(4)
n=3k+2 => 3*3*..*3*(2)