class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if(grid.empty()||grid[0].empty()) return 0;
        int m = grid.size();
        int n = grid[0].size();
        int num = 0;
        vector<vector<int>> visited(m,vector<int>(n,0));
        queue<pair<int,int>> q;
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(grid[i][j]=='1'&&visited[i][j]==0){
                    q.push(make_pair(i,j));
                    visited[i][j] = 1;
                    while(!q.empty()){
                        int i1 = q.front().first;
                        int j1 = q.front().second;
                        q.pop();
                        if(i1>0&&visited[i1-1][j1]==0&&grid[i1-1][j1]=='1'){
                            visited[i1-1][j1] = 1;
                            q.emplace(i1-1,j1);
                        }
                        if(i1<m-1&&visited[i1+1][j1]==0&&grid[i1+1][j1]=='1'){
                            visited[i1+1][j1] = 1;
                            q.emplace(i1+1,j1);
                        }
                        if(j1>0&&visited[i1][j1-1]==0&&grid[i1][j1-1]=='1'){
                            visited[i1][j1-1] = 1;
                            q.emplace(i1,j1-1);
                        }
                        if(j1<n-1&&visited[i1][j1+1]==0&&grid[i1][j1+1]=='1'){
                            visited[i1][j1+1] = 1;
                            q.emplace(i1,j1+1);
                        }
                    }
                    ++num;
                }
            }
        }
        return num;
    }
};
