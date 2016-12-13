class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        table = [[None]*(len(p)+1) for i in range(len(s)+1)]
        return self.isMatchHelper(table,[s],0,[p],0)

    def isMatchHelper(self, table, s, i, p, j):
        if table[i][j]==None:
            if j==len(p[0]):
                table[i][j] = (i==len(s[0]))
            else:
                if j+1<len(p[0]) and p[0][j+1]=='*':
                    for k in range(i,len(s[0])):
                        if p[0][j]!='.' and p[0][j]!=s[0][k]:
                            break
                        if self.isMatchHelper(table,s,k+1,p,j+2):
                            table[i][j] = True
                            break
                    table[i][j] = (table[i][j] or self.isMatchHelper(table,s,i,p,j+2))
                else:
                    table[i][j] = (i<len(s[0]) and (p[0][j]=='.' or p[0][j]==s[0][i]) and self.isMatchHelper(table,s,i+1,p,j+1))
        return table[i][j]
