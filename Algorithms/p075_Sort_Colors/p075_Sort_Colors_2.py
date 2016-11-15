class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j0 = -1
        j1 = -1
        for i in range(0,len(nums)):
            if nums[i]==0:
                j1 += 1
                nums[j1],nums[i] = nums[i],nums[j1]
                j0 += 1
                nums[j0],nums[j1] = nums[j1],nums[j0]
            elif nums[i]==1:
                j1 += 1
                nums[j1],nums[i] = nums[i],nums[j1]
