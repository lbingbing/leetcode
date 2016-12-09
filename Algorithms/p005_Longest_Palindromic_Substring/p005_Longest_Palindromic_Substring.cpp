class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        int start = 0;
        int length = 1;
        vector<vector<int>> isPalindrome(n,vector<int>(n,1));
        for(int i=1;i<n;++i){
            for(int j=0;j<i;++j){
                isPalindrome[j][i] = (s[i]==s[j])&&(j+1>i-1||isPalindrome[j+1][i-1]);
                if(isPalindrome[j][i]&&i-j+1>length){
                    start = j;
                    length = i-j+1;
                }
            }
        }
        return s.substr(start,length);
    }
};
