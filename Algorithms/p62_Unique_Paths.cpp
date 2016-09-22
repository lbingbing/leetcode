class Solution {
public:
    int uniquePaths(int m, int n) {
        if(m<n){
            swap(m,n);
        }
        vector<vector<int>> matrix(m,vector<int>(n,1));
        for(int j=1;j<n;++j){
            matrix[j][j] = matrix[j][j-1]*2;
            for(int i=j+1;i<m;++i){
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1];
            }
        }
        return matrix[m-1][n-1];
    }
};
