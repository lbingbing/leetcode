class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        p_table = [[False for j in range(n)] for i in range(m)]
        a_table = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            if not p_table[i][0]:
                self.flood(matrix,p_table,m,n,i,0)
            if not a_table[i][n-1]:
                self.flood(matrix,a_table,m,n,i,n-1)
        for j in range(n):
            if not p_table[0][j]:
                self.flood(matrix,p_table,m,n,0,j)
            if not a_table[m-1][j]:
                self.flood(matrix,a_table,m,n,m-1,j)
        res = []
        for i in range(m):
            for j in range(n):
                if p_table[i][j] and a_table[i][j]:
                    res.append([i,j])
        return res

    def flood(self, matrix, table, m, n, i, j):
        table[i][j] = True
        if i>0 and not table[i-1][j] and matrix[i][j]<=matrix[i-1][j]:
            self.flood(matrix,table,m,n,i-1,j)
        if i<m-1 and not table[i+1][j] and matrix[i][j]<=matrix[i+1][j]:
            self.flood(matrix,table,m,n,i+1,j)
        if j>0 and not table[i][j-1] and matrix[i][j]<=matrix[i][j-1]:
            self.flood(matrix,table,m,n,i,j-1)
        if j<n-1 and not table[i][j+1] and matrix[i][j]<=matrix[i][j+1]:
            self.flood(matrix,table,m,n,i,j+1)
