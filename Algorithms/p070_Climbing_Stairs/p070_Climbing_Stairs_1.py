class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 1
        else:
            table = [1]*(n+1)
            for i in range(2,n+1):
                table[i] = table[i-1]+table[i-2]
            return table[n]
