class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        m = len(matrix)
        n = len(matrix[0])
        zero_r0 = False
        for j in range(0,n):
            if matrix[0][j]==0:
                zero_r0 = True
        zero_c0 = False
        for i in range(0,m):
            if matrix[i][0]==0:
                zero_c0 = True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j] = 0
        if zero_r0:
            for j in range(0,n):
                matrix[0][j] = 0
        if zero_c0:
            for i in range(0,m):
                matrix[i][0] = 0
