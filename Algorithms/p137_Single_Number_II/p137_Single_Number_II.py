class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        for v in nums:
            b_n = (b&~v)|(a&v)
            a_n = (a&~v)|(~b&~a&v)
            b = b_n
            a = a_n
        return a
