class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> state(n,string(n,'.'));
        solveNQueensHelper(res,state,n,0);
        return res;
    }
    void solveNQueensHelper(vector<vector<string>>& res, vector<string>& state, int n, int l) {
        if(l<n){
            for(int j=0;j<n;++j){
                bool b = 1;
                for(int i=0;i<l;++i){
                    b = b&&(state[i][j]=='.');
                }
                if(!b) continue;
                for(int l1=l-1,j1=j-1;j1>=0&&l1>=0;--l1,--j1){
                    b = b&&(state[l1][j1]=='.');
                }
                if(!b) continue;
                for(int l1=l-1,j1=j+1;j1<n&&l1>=0;--l1,++j1){
                    b = b&&(state[l1][j1]=='.');
                }
                if(!b) continue;
                state[l][j] = 'Q';
                solveNQueensHelper(res,state,n,l+1);
                state[l][j] = '.';
            }
        }else{
            res.push_back(state);
        }
    }
};
