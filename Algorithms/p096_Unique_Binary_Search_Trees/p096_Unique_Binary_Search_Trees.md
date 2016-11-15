Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Solution:
f(n)=
sum{
f(0)*f(n-1)
f(1)*f(n-2)
f(2)*f(n-3)
...
f(n-3)*f(2)
f(n-2)*f(1)
f(n-1)*f(0)
}

f(0)=1