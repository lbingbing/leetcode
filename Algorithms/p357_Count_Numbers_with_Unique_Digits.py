class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        f = 1
        for i in range(0,min(n,10)):
            res += 9*f
            f *= 9-i
        return res
