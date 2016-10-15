class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if(matrix.size()==0) return {};
        vector<int> res(matrix.size()*matrix[0].size());
        int l = 0;
        int r = matrix[0].size()-1;
        int u = 0;
        int d = matrix.size()-1;
        int i = 0;
        while(1){
            if(l>r) break;
            for(int k=l;k<=r;++k){
                res[i++] = matrix[u][k];
            }
            ++u;
            if(u>d) break;
            for(int k=u;k<=d;++k){
                res[i++] = matrix[k][r];
            }
            --r;
            if(l>r) break;
            for(int k=r;k>=l;--k){
                res[i++] = matrix[d][k];
            }
            --d;
            if(u>d) break;
            for(int k=d;k>=u;--k){
                res[i++] = matrix[k][l];
            }
            ++l;
        }
        return res;
    }
};
