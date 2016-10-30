class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        table = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    table[i] = max(table[i],table[j]+1)
        return max(table)
