class Solution {
public:
    int minDistance(string word1, string word2) {
        int n1 = word1.size();
        int n2 = word2.size();
        vector<vector<int>> num(n1+1,vector<int>(n2+1)); // num[i][j]: min distance from word1[0...i-1] to word2[0...j-1]
        for(int i=0;i<=n1;++i){
            num[i][0] = i;
        }
        for(int j=1;j<=n2;++j){
            num[0][j] = j;
        }
        for(int i=1;i<=n1;++i){
            for(int j=1;j<=n2;++j){
                num[i][j] = min({num[i-1][j-1]+(word1[i-1]==word2[j-1]?0:1),num[i-1][j]+1,num[i][j-1]+1});
            }
        }
        return num[n1][n2];
    }
};
