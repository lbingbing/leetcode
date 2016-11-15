class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        state = [['.']*n for i in range(0,n)]
        self.solveNQueensHelper(res,state,n,0)
        return res
        
    def solveNQueensHelper(self, res, state, n, l):
        if l<n:
            for j in range(0,n):
                b = True
                for i in range(0,l):
                    b = b and (state[i][j]=='.')
                if not b:
                    continue
                l1 = l-1
                j1 = j-1
                while j1>=0 and l1>=0:
                    b = b and (state[l1][j1]=='.')
                    l1 -= 1
                    j1 -= 1
                if not b:
                    continue
                l1 = l-1
                j1 = j+1
                while j1<n and l1>=0:
                    b = b and (state[l1][j1]=='.')
                    l1 -= 1
                    j1 += 1
                if not b:
                    continue
                state[l][j] = 'Q'
                self.solveNQueensHelper(res,state,n,l+1)
                state[l][j] = '.'
        else:
            res.append([''.join(state[i]) for i in range(0,n)])
