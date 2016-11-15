Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
162 + 0^2 + 0^2 = 1

Solution:
Max 32-bit signed int is 2147483647(0x7FFFFFFF), of which digit width is 10.
So the upper bound of 1-step result is 10*9^2=810, which is also the upper bound of all possible results.
Then we can keep on the transformation and finally find "1" cases or catch "cyclic" cases by a table no larger than the upper bound.