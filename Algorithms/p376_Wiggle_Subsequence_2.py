class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 1
        tail = 0 # 0:eq, 1:inc, 2:dec
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1] and tail!=1:
                res += 1
                tail = 1
            elif nums[i]<nums[i-1] and tail!=2:
                res += 1
                tail = 2
        return res
