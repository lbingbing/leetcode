class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        zs = 0
        for v in nums:
            if v==0:
                break
            else:
                zs += 1
        
        for i in range(zs+1,nums_len):
            if nums[i]!=0:
                nums[zs], nums[i] = nums[i], nums[zs]
                zs += 1
