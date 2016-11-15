class Solution {
public:
    vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if(matrix.empty()||matrix[0].empty()) return {};
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<bool>> p_table(m,vector<bool>(n,0));
        vector<vector<bool>> a_table(m,vector<bool>(n,0));
        for(int i=0;i<m;++i){
            if(!p_table[i][0])   flood(matrix,p_table,m,n,i,0);
            if(!a_table[i][n-1]) flood(matrix,a_table,m,n,i,n-1);
        }
        for(int j=0;j<n;++j){
            if(!p_table[0][j])   flood(matrix,p_table,m,n,0,j);
            if(!a_table[m-1][j]) flood(matrix,a_table,m,n,m-1,j);
        }
        vector<pair<int,int>> res;
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(p_table[i][j]&&a_table[i][j]) res.emplace_back(i,j);
            }
        }
        return res;
    }
    void flood(vector<vector<int>>& matrix, vector<vector<bool>>& table, int m, int n, int i, int j) {
        table[i][j] = 1;
        if(i>0  &&!table[i-1][j]&&matrix[i][j]<=matrix[i-1][j]) flood(matrix,table,m,n,i-1,j);
        if(i<m-1&&!table[i+1][j]&&matrix[i][j]<=matrix[i+1][j]) flood(matrix,table,m,n,i+1,j);
        if(j>0  &&!table[i][j-1]&&matrix[i][j]<=matrix[i][j-1]) flood(matrix,table,m,n,i,j-1);
        if(j<n-1&&!table[i][j+1]&&matrix[i][j]<=matrix[i][j+1]) flood(matrix,table,m,n,i,j+1);
    }
};
