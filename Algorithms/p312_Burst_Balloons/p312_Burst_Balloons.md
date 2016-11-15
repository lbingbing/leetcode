Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ¡Ü n ¡Ü 500, 0 ¡Ü nums[i] ¡Ü 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

Solution:
let nums={1,nums,1} for simplicity.
let f(i,j) be the optimal result of subsequence of nums between i and j. So f(1,n) is the answer.
then
f(i,j)=
max{nums[i-1]*nums[k]*nums[j+1]+f(i,k-1)+f(k+1,j)}, if i<=k<=j (k is the last picked element)
0, if i=j+1 (for simplicity)
don't care, if i>j+1 (don't need to calculate & record)