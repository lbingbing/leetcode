class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        table = [[None]*(len(p)+1) for i in range(len(s)+1)]
        return self.isMatchHelper(table,[s],len(s),[p],len(p))

    def isMatchHelper(self, table, s, i, p, j):
        if table[i][j]==None:
            if j==0:
                table[i][j] = (i==0)
            else:
                if p[0][j-1]=='*':
                    for k in range(i-1,-1,-1):
                        if p[0][j-2]!='.' and p[0][j-2]!=s[0][k]:
                            break
                        if self.isMatchHelper(table,s,k,p,j-2):
                            table[i][j] = True
                            break
                    table[i][j] = (table[i][j] or self.isMatchHelper(table,s,i,p,j-2))
                else:
                    table[i][j] = (i>0 and (p[0][j-1]=='.' or p[0][j-1]==s[0][i-1]) and self.isMatchHelper(table,s,i-1,p,j-1))
        return table[i][j]
