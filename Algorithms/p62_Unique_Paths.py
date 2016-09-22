class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m<n:
            m,n = n,m
        matrix = [[1 for j in range(0,n)] for i in range(0,m)]
        for j in range(1,n):
            matrix[j][j] = matrix[j][j-1]*2
            for i in range(j+1,m):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]
