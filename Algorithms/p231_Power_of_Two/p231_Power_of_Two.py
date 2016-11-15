class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>1:
            if n>>1<<1!=n:
                return False
            n >>= 1
        return n>0
