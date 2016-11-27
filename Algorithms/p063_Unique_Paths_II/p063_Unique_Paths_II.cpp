class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if(obstacleGrid.empty()||obstacleGrid[0].empty()) return 0;
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> path_num(m,vector<int>(n,0));
        path_num[0][0] = obstacleGrid[0][0]==0 ? 1:0;
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(obstacleGrid[i][j]==0){
                    if(i>0) path_num[i][j] += path_num[i-1][j];
                    if(j>0) path_num[i][j] += path_num[i][j-1];
                }
            }
        }
        return path_num[m-1][n-1];
    }
};
