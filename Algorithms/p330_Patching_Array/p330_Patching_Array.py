class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        add = 0
        max_n = 0
        i = 0
        while max_n<n:
            if i==len(nums) or nums[i]>max_n+1:
                max_n += max_n+1
                add += 1
            else:
                max_n += nums[i]
                i += 1
        return add
