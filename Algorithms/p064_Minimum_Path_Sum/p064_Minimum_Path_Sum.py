class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        table = [None]*n
        table[0] = grid[0][0]
        for j in range(1,n):
            table[j] = table[j-1]+grid[0][j]
        for i in range(1,m):
            table[0] = table[0]+grid[i][0]
            for j in range(1,n):
                table[j] = min(table[j],table[j-1])+grid[i][j]
        return table[n-1]
