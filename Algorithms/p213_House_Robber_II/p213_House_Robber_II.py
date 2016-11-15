class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        # res0: no robbing on 1st day
        # res1: robbing on 1st day
        res0_1 = 0
        res0_2 = nums[1]
        res1_1 = nums[0]
        res1_2 = nums[0]
        for i in range(2,len(nums)):
            res0_1, res0_2 = res0_2, max(res0_1+nums[i],res0_2)
            res1_1, res1_2 = res1_2, max(res1_1+nums[i],res1_2)
        return max(res0_2,res1_1)
