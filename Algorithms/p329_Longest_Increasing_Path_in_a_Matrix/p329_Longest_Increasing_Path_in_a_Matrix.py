class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        table = [[0 for j in range(n)] for i in range(m)] # max length of sequences starting with [i,j]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res,self.get_max_len(matrix,table,i,j))
        return res

    def get_max_len(self, matrix, table, i, j):
        if table[i][j]>0:
            return table[i][j]
        res = 1
        if i>0 and matrix[i][j]<matrix[i-1][j]:
            res = max(res,self.get_max_len(matrix,table,i-1,j)+1)
        if i<len(matrix)-1 and matrix[i][j]<matrix[i+1][j]:
            res = max(res,self.get_max_len(matrix,table,i+1,j)+1)
        if j>0 and matrix[i][j]<matrix[i][j-1]:
            res = max(res,self.get_max_len(matrix,table,i,j-1)+1)
        if j<len(matrix[0])-1 and matrix[i][j]<matrix[i][j+1]:
            res = max(res,self.get_max_len(matrix,table,i,j+1)+1)
        table[i][j] = res
        return res
