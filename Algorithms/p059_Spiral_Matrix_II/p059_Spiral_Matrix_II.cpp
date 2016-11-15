class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n,vector<int>(n));
        int l = 0;
        int r = n-1;
        int u = 0;
        int d = n-1;
        int i = 0;
        while(1){
            if(l>r) break;
            for(int k=l;k<=r;++k){
                res[u][k] = ++i;
            }
            ++u;
            if(u>d) break;
            for(int k=u;k<=d;++k){
                res[k][r] = ++i;
            }
            --r;
            if(l>r) break;
            for(int k=r;k>=l;--k){
                res[d][k] = ++i;
            }
            --d;
            if(u>d) break;
            for(int k=d;k>=u;--k){
                res[k][l] = ++i;
            }
            ++l;
        }
        return res;
    }
};
