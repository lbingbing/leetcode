class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[None for j in range(0,n)] for i in range(0,n)]
        l = 0
        r = n-1
        u = 0
        d = n-1
        i = 0
        while True:
            if l>r:
                break
            for k in range(l,r+1):
                i += 1
                res[u][k] = i
            u += 1
            if u>d:
                break
            for k in range(u,d+1):
                i += 1
                res[k][r] = i
            r -= 1
            if l>r:
                break
            for k in range(r,l-1,-1):
                i += 1
                res[d][k] = i
            d -= 1
            if u>d:
                break
            for k in range(d,u-1,-1):
                i += 1
                res[k][l] = i
            l += 1
        return res
