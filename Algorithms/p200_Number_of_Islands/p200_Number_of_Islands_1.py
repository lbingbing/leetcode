class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        num = 0
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:
                    self.dfs(grid,visited,m,n,i,j)
                    num += 1
        return num

    def dfs(self, grid, visited, m, n, i, j):
        visited[i][j] = True
        if i>0 and not visited[i-1][j] and grid[i-1][j]=='1':
            self.dfs(grid,visited,m,n,i-1,j)
        if i<m-1 and not visited[i+1][j] and grid[i+1][j]=='1':
            self.dfs(grid,visited,m,n,i+1,j)
        if j>0 and not visited[i][j-1] and grid[i][j-1]=='1':
            self.dfs(grid,visited,m,n,i,j-1)
        if j<n-1 and not visited[i][j+1] and grid[i][j+1]=='1':
            self.dfs(grid,visited,m,n,i,j+1)
