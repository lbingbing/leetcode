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
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not visited[i][j]:
                    q.append((i,j))
                    visited[i][j] = True
                    while q:
                        i1,j1 = q.popleft()
                        if i1>0 and not visited[i1-1][j1] and grid[i1-1][j1]=='1':
                            visited[i1-1][j1] = True
                            q.append((i1-1,j1))
                        if i1<m-1 and not visited[i1+1][j1] and grid[i1+1][j1]=='1':
                            visited[i1+1][j1] = True
                            q.append((i1+1,j1))
                        if j1>0 and not visited[i1][j1-1] and grid[i1][j1-1]=='1':
                            visited[i1][j1-1] = True
                            q.append((i1,j1-1))
                        if j1<n-1 and not visited[i1][j1+1] and grid[i1][j1+1]=='1':
                            visited[i1][j1+1] = True
                            q.append((i1,j1+1))
                    num += 1
        return num
