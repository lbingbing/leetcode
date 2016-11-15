class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n
        while l<r:
            mid = (l+r)//2
            i = mid//n
            j = mid%n
            if matrix[i][j]<target:
                l = mid+1
            elif matrix[i][j]>target:
                r = mid
            else:
                return True
        return False
