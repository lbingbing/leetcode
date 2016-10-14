Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ¡Ü i < j < k ¡Ü n-1 else return false.

Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

Solution:
generalized problem should be 'subsequence of length k'.

v_vld[i]: increasing subsequence of length i found yet or not, 1<=i<k
v[i]: last number of increasing subsequence of length i, 1<=i<k

for all v_vld, if v_vld[j]==1&&j>i, then v_vld[i]==1
for all valid v[i], v[1]<v[2]<v[3]<...<v[k-1]

scan the array and update v[i]. once all v_vld[i] are set and a number from the array greater than v[k-1], the increasing subsequence exists.
(to get rid of v_vld[i], v[i] can be initialized with maxinum value of its variable type)