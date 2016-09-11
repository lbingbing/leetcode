class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>=3:
            if n//3*3!=n:
                return False
            n //= 3
        return n==1
