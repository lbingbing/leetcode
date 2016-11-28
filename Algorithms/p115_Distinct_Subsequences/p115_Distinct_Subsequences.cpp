class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.size();
        int n = t.size();
        vector<vector<int>> num(m+1,vector<int>(n+1,0));
        num[0][0] = 1;
        for(int i=1;i<=m;++i){
            num[i][0] = 1;
            for(int j=1;j<=i&&j<=n;++j){
                num[i][j] = num[i-1][j];
                if(s[i-1]==t[j-1]) num[i][j] += num[i-1][j-1];
            }
        }
        return num[m][n];
    }
};
