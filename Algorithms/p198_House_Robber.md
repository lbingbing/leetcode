You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Solution 1:
f[i]=max(nums[i]+f[i-2],f[i-1])

Solution 2:
s0: no robbing
s1: robbing

s0[i]=max(s0[i-1],s1[i-1])
s1[i]=p[i]+s0[i-1]

f[i]=max(s0[i],s1[i])