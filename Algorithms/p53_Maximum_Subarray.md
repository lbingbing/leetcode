Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Solution:
f0[i]: max within [0,i] when not ending with nums[i]
f1[i]: max within [0,i] when ending with nums[i]

f0[i]=
max(f0[i-1],f1[i-1]), i>=2
muns[0], i=1
meaningless (or minus infinity for simplicity), i=0
f1[i]=
nums[i]+max(f1[i-1],0), i>=1
nums[0], i=0

res=max(f0[n-1],f1[n-1])