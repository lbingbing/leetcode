class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [None]*n
        i = [0]
        for j in range(1,min(10,n+1)):
            self.lexicalOrderHelper(res,i,n,j)
        return res
        
    def lexicalOrderHelper(self, res, i, n, m):
        res[i[0]] = m
        i[0] += 1
        m *= 10
        for j in range(0,10):
            if m+j>n:
                break
            self.lexicalOrderHelper(res,i,n,m+j)
