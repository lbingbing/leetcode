class Solution {
public:
    int longestPalindrome(string s) {
        array<int,256> cnt = {};
        for(char c : s){
            ++cnt[c];
        }
        int res = 0;
        int has_odd = 0;
        for(int num : cnt){
            res += num/2*2;
            has_odd |= num&0x1;
        }
        return res+has_odd;
    }
};
