class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res1 = 0
        res2 = 0
        for v in nums:
            res1, res2 = res2, max(res1+v,res2)
        return res2
