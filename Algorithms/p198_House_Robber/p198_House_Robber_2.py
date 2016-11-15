class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s0 = 0 # no robbing
        s1 = 0 # robbing
        for v in nums:
            s0, s1 = max(s0,s1), s0+v
        return max(s0,s1)
