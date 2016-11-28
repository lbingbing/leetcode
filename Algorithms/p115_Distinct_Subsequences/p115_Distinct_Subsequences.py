class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        num = [[0 for j in range(n+1)] for i in range(m+1)]
        num[0][0] = 1
        for i in range(1,m+1):
            num[i][0] = 1
            for j in range(1,min(i,n)+1):
                num[i][j] = num[i-1][j]
                if s[i-1]==t[j-1]:
                    num[i][j] += num[i-1][j-1]
        return num[m][n]
