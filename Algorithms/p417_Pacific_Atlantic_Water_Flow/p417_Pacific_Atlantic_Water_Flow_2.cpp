class Solution {
public:
    vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
        if(matrix.empty()||matrix[0].empty()) return {};
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<bool>> p_table(m,vector<bool>(n,0));
        vector<vector<bool>> a_table(m,vector<bool>(n,0));
        queue<pair<int,int>> q_p;
        queue<pair<int,int>> q_a;
        for(int i=0;i<m;++i){
            if(!p_table[i][0]){
                p_table[i][0] = 1;
                q_p.emplace(i,0);
            }
            if(!a_table[i][n-1]){
                a_table[i][n-1] = 1;
                q_a.emplace(i,n-1);
            }
        }
        for(int j=0;j<n;++j){
            if(!p_table[0][j]){
                p_table[0][j] = 1;
                q_p.emplace(0,j);
            }
            if(!a_table[m-1][j]){
                a_table[m-1][j] = 1;
                q_a.emplace(m-1,j);
            }
        }
        flood(matrix,p_table,q_p,m,n);
        flood(matrix,a_table,q_a,m,n);
        vector<pair<int,int>> res;
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(p_table[i][j]&&a_table[i][j]) res.emplace_back(i,j);
            }
        }
        return res;
    }
    void flood(vector<vector<int>>& matrix, vector<vector<bool>>& table, queue<pair<int,int>>& q, int m, int n) {
        while(!q.empty()){
            int i = q.front().first;
            int j = q.front().second;
            q.pop();
            if(i>0&&!table[i-1][j]&&matrix[i][j]<=matrix[i-1][j]){
                table[i-1][j] = 1;
                q.emplace(i-1,j);
            }
            if(i<m-1&&!table[i+1][j]&&matrix[i][j]<=matrix[i+1][j]){
                table[i+1][j] = 1;
                q.emplace(i+1,j);
            }
            if(j>0&&!table[i][j-1]&&matrix[i][j]<=matrix[i][j-1]){
                table[i][j-1] = 1;
                q.emplace(i,j-1);
            }
            if(j<n-1&&!table[i][j+1]&&matrix[i][j]<=matrix[i][j+1]){
                table[i][j+1] = 1;
                q.emplace(i,j+1);
            }
        }
    }
};
