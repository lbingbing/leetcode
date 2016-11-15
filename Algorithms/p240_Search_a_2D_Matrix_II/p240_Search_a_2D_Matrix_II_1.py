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
        h = (n>m)
        bound1 = n if h else m
        bound2 = m if h else n
        end=bound1
        for k in range(0,bound2):
            low = 0
            high = end
            while low<high:
                mid = (low+high)//2
                v = matrix[k][mid] if h else matrix[mid][k]
                if v<target:
                    low = mid+1
                elif v>target:
                    high = mid
                else:
                    return True
            end = low
        return False
