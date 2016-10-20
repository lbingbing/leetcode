class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if(grid.size()==0 || grid[0].size()==0) return 0;
        int m = grid.size();
        int n = grid[0].size();
        vector<int> table(n);
        table[0] = grid[0][0];
        for(int j=1;j<n;++j){
            table[j] = table[j-1]+grid[0][j];
        }
        for(int i=1;i<m;++i){
            table[0] = table[0]+grid[i][0];
            for(int j=1;j<n;++j){
                table[j] = min(table[j],table[j-1])+grid[i][j];
            }
        }
        return table[n-1];
    }
};
