class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]
        state = [[False]*n for i in range(0,n)]
        self.totalNQueensHelper(res,state,n,0)
        return res[0]
        
    def totalNQueensHelper(self, res, state, n, l):
        if l<n:
            for j in range(0,n):
                b = True
                for i in range(0,l):
                    b = b and not state[i][j]
                if not b:
                    continue
                l1 = l-1
                j1 = j-1
                while j1>=0 and l1>=0:
                    b = b and not state[l1][j1]
                    l1 -= 1
                    j1 -= 1
                if not b:
                    continue
                l1 = l-1
                j1 = j+1
                while j1<n and l1>=0:
                    b = b and not state[l1][j1]
                    l1 -= 1
                    j1 += 1
                if not b:
                    continue
                state[l][j] = True
                self.totalNQueensHelper(res,state,n,l+1)
                state[l][j] = False
        else:
            res[0] += 1
