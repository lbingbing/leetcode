class Solution {
public:
    char findTheDifference(string s, string t) {
        vector<int> cnt(256);
        for(char c : s){
            cnt[c]++;
        }
        for(char c : t){
            if(cnt[c]==0){
                return c;
            }
            cnt[c]--;
        }
        return static_cast<char>(0);
    }
};
