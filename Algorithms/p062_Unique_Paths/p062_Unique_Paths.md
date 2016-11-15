A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

+-+-+-+-+-+-+-+
|S|0|0|0|0|0|0|
+-+-+-+-+-+-+-+
|0|0|0|0|0|0|0|
+-+-+-+-+-+-+-+
|0|0|0|0|0|0|F|
+-+-+-+-+-+-+-+

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Solution:
f(m,n)=
f(m-1,n)+f(m,n-1), m>1 && n>1
1, m=1 || n=1

f(m,n)=f(n,m)

(i,j)
11
21 22
31 32 33
41 42 43
51 52 53
61 62 63
71 72 73

DP:
11->21->31->41->51->61->71
22->32->42->52->62->72
33->43->53->63->73