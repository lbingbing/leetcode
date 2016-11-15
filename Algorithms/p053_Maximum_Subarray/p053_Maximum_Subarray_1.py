class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        # res0: max within [0,i] when not ending with nums[i]
        # res1: max within [0,i] when ending with nums[i]
        res0 = nums[0]
        res1 = nums[1]+max(nums[0],0)
        for i in range(2,len(nums)):
            res0 = max(res0,res1)
            res1 = nums[i]+max(res1,0)
        return max(res0,res1)
