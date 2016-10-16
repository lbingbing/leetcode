class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size()==0) return 0;
        int m = matrix.size();
        int n = matrix[0].size();
        bool h = (n>m);
        int bound1 = h ? n : m;
        int bound2 = h ? m : n;
        for(int k=0,end=bound1;k<bound2;++k){
            int low = 0;
            int high = end;
            while(low<high){
                int mid = (low+high)/2;
                int v = h ? matrix[k][mid] : matrix[mid][k];
                if(v<target){
                    low = mid+1;
                }else if(v>target){
                    high = mid;
                }else{
                    return 1;
                }
            }
            end = low;
        }
        return 0;
    }
};
