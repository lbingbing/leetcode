Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Solution:
make a array of similar state machines, let numbers from the array be a stream of input (each bit of a number for each state machine).
make bit 0/1 of the majority munbers leave the state machine in reset state.
make bit 0 of the minority number leave the state machine in reset state.
make bit 1 of the minority number leave the state machine in a non-reset state.
then non-reset state machine indicates bit 1 in corresponding position of the minority number.
this stategy can solve any n-m problem (n majority, m minority), except n is a factor of m (in this case, any state machine, that can be reset by majority number, can also be reset by minority number).

for this 3-1 case, use two bits state
s0=00
s1=01
s2=10

let v be input bit:
(s,v)->(s_next)
s0,0->s0
s1,0->s1
s2,0->s2
s0,1->s1
s1,1->s2
s2,1->s0

assume b=s[1],a=s[0]:
(b,a,v)->(b_next,a_next)
000->00
010->01
100->10
110->xx
001->01
011->10
101->00
111->xx

b_next=b~v+av
a_next=a~v+~b~av