class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        res = [None]*(len(matrix)*len(matrix[0]))
        l = 0
        r = len(matrix[0])-1
        u = 0
        d = len(matrix)-1
        i = 0
        while True:
            if l>r:
                break
            for k in range(l,r+1):
                res[i] = matrix[u][k]
                i += 1
            u += 1
            if u>d:
                break
            for k in range(u,d+1):
                res[i] = matrix[k][r]
                i += 1
            r -= 1
            if l>r:
                break
            for k in range(r,l-1,-1):
                res[i] = matrix[d][k]
                i += 1
            d -= 1
            if u>d:
                break
            for k in range(d,u-1,-1):
                res[i] = matrix[k][l]
                i += 1
            l += 1
        return res
