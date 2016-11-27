class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        path_num = [[0 for j in range(n)] for i in range(m)]
        path_num[0][0] = 1 if obstacleGrid[0][0]==0 else 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==0:
                    if i>0:
                        path_num[i][j] += path_num[i-1][j]
                    if j>0:
                        path_num[i][j] += path_num[i][j-1]
        return path_num[m-1][n-1]
