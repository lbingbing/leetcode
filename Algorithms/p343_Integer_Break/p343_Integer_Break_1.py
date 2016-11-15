class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0]*(n+1)
        g = [0]*(n+1)
        g[1] = 1
        for i in range(2,n+1):
            for j in range(1,i):
                v = j*g[i-j]
                if v>f[i]:
                    f[i] = v
            g[i] = max(i,f[i])
        return f[n]
