There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3. 

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.

Solution:
position[i](i within [1,n]) is 1 only when i has odd number of divisors (including 1 and i).
let m = number of n's divisors
1.n is prime number:
m = 2 (1 and n)
2.n is composite number:
1) non-square number:
each divisor k (including 1 and n) has its counterpart (n/k)
so m is even number, position[n]=0
2) square number:
each divisor k (including 1 and n) has its counterpart (n/k), except sqrt(n)
so m is odd number, position[n]=1
so
f(1)=1
f(2)=f(1)
f(3)=f(1)
f(4)=2
f(5)=f(4)
f(6)=f(4)
f(7)=f(4)
f(8)=f(4)
f(9)=3
...
f(n)=int(sqrt(n))