class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<int>> table(s.size()+1,vector<int>(p.size()+1,-1));
        return isMatchHelper(table,s,0,p,0);
    }
    bool isMatchHelper(vector<vector<int>>& table, string& s, int i, string& p, int j) {
        if(table[i][j]==-1){
            if(j==p.size()){
                table[i][j] = (i==s.size());
            }else{
                if(j+1<p.size()&&p[j+1]=='*'){
                    for(int k=i;k<s.size()&&(p[j]=='.'||p[j]==s[k]);++k){
                        if(isMatchHelper(table,s,k+1,p,j+2)){
                            table[i][j] = 1;
                            break;
                        }
                    }
                    table[i][j] = (table[i][j]==1||isMatchHelper(table,s,i,p,j+2));
                }else{
                    table[i][j] = (i<s.size()&&(p[j]=='.'||p[j]==s[i])&&isMatchHelper(table,s,i+1,p,j+1));
                }
            }
        }
        return table[i][j]==1;
    }
};
