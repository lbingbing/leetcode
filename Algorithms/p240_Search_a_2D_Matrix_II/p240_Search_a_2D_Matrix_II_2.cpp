class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size()==0) return 0;
        int m = matrix.size();
        int n = matrix[0].size();
        for(int i=0,j=n-1;i<m&&j>=0;){
            if(matrix[i][j]<target){
                ++i;
            }else if(matrix[i][j]>target){
                --j;
            }else{
                return 1;
            }
        }
        return 0;
    }
};
