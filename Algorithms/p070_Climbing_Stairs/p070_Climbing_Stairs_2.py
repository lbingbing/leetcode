class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        v1 = 1
        v2 = 1
        for i in range(2,n+1):
            v1,v2 = v2,v1+v2
        return v2
