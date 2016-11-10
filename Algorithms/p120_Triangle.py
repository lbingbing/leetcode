class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        table = [0]*n
        table_tmp = [0]*n
        table[0] = triangle[0][0]
        for i in range(1,n):
            table_tmp[0] = table[0]+triangle[i][0]
            for j in range(1,i):
                table_tmp[j] = min(table[j-1],table[j])+triangle[i][j]
            table_tmp[i] = table[i-1]+triangle[i][i]
            for j in range(i+1):
                table[j] = table_tmp[j]
        return min(table)
