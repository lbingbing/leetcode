class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<int>> table(s.size()+1,vector<int>(p.size()+1,-1));
        return isMatchHelper(table,s,s.size(),p,p.size());
    }
    bool isMatchHelper(vector<vector<int>>& table, string& s, int i, string& p, int j) {
        if(table[i][j]==-1){
            if(j==0){
                table[i][j] = (i==0);
            }else{
                if(p[j-1]=='*'){
                    for(int k=i-1;k>=0&&(p[j-2]=='.'||p[j-2]==s[k]);--k){
                        if(isMatchHelper(table,s,k,p,j-2)){
                            table[i][j] = 1;
                            break;
                        }
                    }
                    table[i][j] = (table[i][j]==1||isMatchHelper(table,s,i,p,j-2));
                }else{
                    return i>0&&(p[j-1]=='.'||p[j-1]==s[i-1])&&isMatchHelper(table,s,i-1,p,j-1);
                }
            }
        }
        return table[i][j];
    }
};
