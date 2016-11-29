class Solution {
public:
    int minCut(string s) {
        if(s.empty()) return 0;
        int n = s.size();
        vector<int> cut_num(n+1); // cut_num[i]: min cut num of s[0,i-1]
        vector<vector<int>> isPalindrome(n,vector<int>(n)); // isPalindrome[i][j]: s[i,j] is palindrome
        cut_num[0] = -1;
        for(int j=0;j<n;++j){
            cut_num[j+1] = j;
            for(int i=0;i<=j;++i){
                isPalindrome[i][j] = (s[i]==s[j]&&(i+1>=j-1||isPalindrome[i+1][j-1]));
                if(isPalindrome[i][j]){
                    cut_num[j+1] = min(cut_num[j+1],cut_num[i]+1);
                }
            }
        }
        return cut_num[n];
    }
};
