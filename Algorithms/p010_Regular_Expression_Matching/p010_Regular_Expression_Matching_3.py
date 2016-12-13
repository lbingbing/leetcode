class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        table = [[False]*(n+1) for i in range(m+1)]
        table[0][0] = True
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1]=='*':
                    table[i][j] = table[i][j-2] or (i>0 and (p[j-2]=='.' or p[j-2]==s[i-1]) and table[i-1][j])
                else:
                    table[i][j] = i>0 and (p[j-1]=='.' or p[j-1]==s[i-1]) and table[i-1][j-1]
        return table[m][n]
