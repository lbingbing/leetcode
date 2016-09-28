Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Solution:
f0[i]: max amount of money within house [0,i] when no robbing for 1st house
f1[i]: max amount of money within house [0,i] when robbing for 1st house

f0[i]=
max(f0[i-2]+nums[i],f0[i-1]), i>=2
nums[1], i=1
0, i=0
f1[i]=
max(f1[i-2]+nums[i],f1[i-1]), i>=2
nums[0], i=0,1

res=max(f0[n-1],f1[n-2])