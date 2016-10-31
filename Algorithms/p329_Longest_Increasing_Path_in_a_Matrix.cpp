class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if(matrix.empty()||matrix[0].empty()) return 0;
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> table(m,vector<int>(n,0)); // max length of sequences starting with [i,j]
        int res = 0;
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                res = max(res,get_max_len(matrix,table,i,j));
            }
        }
        return res;
    }
    int get_max_len(vector<vector<int>>& matrix, vector<vector<int>>& table, int i, int j) {
        if(table[i][j]>0) return table[i][j];
        int res = 1;
        if(i>0&&matrix[i][j]<matrix[i-1][j]){
            res = max(res,get_max_len(matrix,table,i-1,j)+1);
        }
        if(i<matrix.size()-1&&matrix[i][j]<matrix[i+1][j]){
            res = max(res,get_max_len(matrix,table,i+1,j)+1);
        }
        if(j>0&&matrix[i][j]<matrix[i][j-1]){
            res = max(res,get_max_len(matrix,table,i,j-1)+1);
        }
        if(j<matrix[0].size()-1&&matrix[i][j]<matrix[i][j+1]){
            res = max(res,get_max_len(matrix,table,i,j+1)+1);
        }
        table[i][j] = res;
        return res;
    }
};
