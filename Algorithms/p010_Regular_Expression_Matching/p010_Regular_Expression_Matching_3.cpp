class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size();
        int n = p.size();
        vector<vector<int>> table(m+1,vector<int>(n+1,0));
        table[0][0] = 1;
        for(int i=0;i<=m;++i){
            for(int j=1;j<=n;++j){
                if(p[j-1]=='*'){
                    table[i][j] = table[i][j-2]||i>0&&(p[j-2]=='.'||p[j-2]==s[i-1])&&table[i-1][j];
                }else{
                    table[i][j] = i>0&&(p[j-1]=='.'||p[j-1]==s[i-1])&&table[i-1][j-1];
                }
            }
        }
        return table[m][n];
    }
};
