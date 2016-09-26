class Solution {
public:
    int totalNQueens(int n) {
        int res = 0;
        vector<vector<int>> state(n,vector<int>(n,0));
        totalNQueensHelper(res,state,n,0);
        return res;
    }
    void totalNQueensHelper(int& res, vector<vector<int>>& state, int n, int l) {
        if(l<n){
            for(int j=0;j<n;++j){
                bool b = 1;
                for(int i=0;i<l;++i){
                    b = b&&!state[i][j];
                }
                if(!b) continue;
                for(int l1=l-1,j1=j-1;j1>=0&&l1>=0;--l1,--j1){
                    b = b&&!state[l1][j1];
                }
                if(!b) continue;
                for(int l1=l-1,j1=j+1;j1<n&&l1>=0;--l1,++j1){
                    b = b&&!state[l1][j1];
                }
                if(!b) continue;
                state[l][j] = 1;
                totalNQueensHelper(res,state,n,l+1);
                state[l][j] = 0;
            }
        }else{
            ++res;
        }
    }
};
