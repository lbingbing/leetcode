class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        w = len(nums)
        n = 0x1<<w
        res = [[] for i in range(0,n)]
        for i in range(0,n):
            for j in range(w-1,-1,-1):
                if i&(0x1<<j):
                    res[i].append(nums[w-1-j])
        return res
