class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if(grid.empty()||grid[0].empty()) return 0;
        int m = grid.size();
        int n = grid[0].size();
        int num = 0;
        vector<vector<int>> visited(m,vector<int>(n,0));
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(grid[i][j]=='1'&&visited[i][j]==0){
                    dfs(grid,visited,m,n,i,j);
                    ++num;
                }
            }
        }
        return num;
    }
    void dfs(vector<vector<char>>& grid, vector<vector<int>>& visited, int m, int n, int i, int j) {
        visited[i][j] = 1;
        if(i>0  &&visited[i-1][j]==0&&grid[i-1][j]=='1') dfs(grid,visited,m,n,i-1,j);
        if(i<m-1&&visited[i+1][j]==0&&grid[i+1][j]=='1') dfs(grid,visited,m,n,i+1,j);
        if(j>0  &&visited[i][j-1]==0&&grid[i][j-1]=='1') dfs(grid,visited,m,n,i,j-1);
        if(j<n-1&&visited[i][j+1]==0&&grid[i][j+1]=='1') dfs(grid,visited,m,n,i,j+1);
    }
};
