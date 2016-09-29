class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        res = self.getMaxSubArray(nums,len(nums)-1)
        return max(res[0],res[1])
        
    def getMaxSubArray(self, nums, i):
        """
        :rtype: tuple[int,int]
            [0]: max within [0,i] when not ending with nums[i]
            [1]: max within [0,i] when ending with nums[i]
        """
        if i>=2:
            res = self.getMaxSubArray(nums,i-1)
            return (max(res[0],res[1]),nums[i]+max(res[1],0))
        else:
            return (nums[0],nums[1]+max(nums[0],0))
