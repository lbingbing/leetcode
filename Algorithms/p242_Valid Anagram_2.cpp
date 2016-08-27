class Solution {
public:
    bool isAnagram(string s, string t) {
        int cnt1[256] = {};
        int cnt2[256] = {};
        for(const char& c : s){
            cnt1[c]++;
        }
        for(const char& c : t){
            cnt2[c]++;
        }
        for(int i=0;i<256;i++){
            if(cnt1[i]!=cnt2[i]){
                return 0;
            }
        }
        return 1;
    }
};
