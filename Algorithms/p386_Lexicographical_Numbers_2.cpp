class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> res(n);
        int i = 0;
        for(int j=1;j<10&&j<=n;++j){
            lexicalOrderHelper(res,i,n,j);
        }
        return res;
    }
    void lexicalOrderHelper(vector<int>& res, int& i, int n, int m) {
        res[i++] = m;
        for(int j=0;j<10&&m*10+j<=n;++j){
            lexicalOrderHelper(res,i,n,m*10+j);
        }
    }
};
