class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size()==0) return 0;
        int m = matrix.size();
        int n = matrix[0].size();
        int l = 0;
        int r = m*n;
        while(l<r){
            int mid = (l+r)/2;
            int i = mid/n;
            int j = mid%n;
            if(matrix[i][j]<target){
                l = mid+1;
            }else if(matrix[i][j]>target){
                r = mid;
            }else{
                return 1;
            }
        }
        return 0;
    }
};
