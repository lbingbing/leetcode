class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if(matrix.empty()||matrix[0].empty()) return;
        int m = matrix.size();
        int n = matrix[0].size();
        bool zero_r0 = 0;
        for(int j=0;j<n;++j){
            if(matrix[0][j]==0) zero_r0 = 1;
        }
        bool zero_c0 = 0;
        for(int i=0;i<m;++i){
            if(matrix[i][0]==0) zero_c0 = 1;
        }
        for(int i=1;i<m;++i){
            for(int j=1;j<n;++j){
                if(matrix[i][j]==0){
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        for(int i=1;i<m;++i){
            for(int j=1;j<n;++j){
                if(matrix[0][j]==0||matrix[i][0]==0){
                    matrix[i][j] = 0;
                }
            }
        }
        if(zero_r0){
            for(int j=0;j<n;++j){
                matrix[0][j] = 0;
            }
        }
        if(zero_c0){
            for(int i=0;i<m;++i){
                matrix[i][0] = 0;
            }
        }
    }
};
