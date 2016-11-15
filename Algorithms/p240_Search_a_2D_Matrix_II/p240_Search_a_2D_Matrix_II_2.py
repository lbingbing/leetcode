class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        while i<m and j>=0:
            if matrix[i][j]<target:
                i += 1
            elif matrix[i][j]>target:
                j -= 1
            else:
                return True
        return False
