class Solution {
public:
    int titleToNumber(string s) {
        int res = 0;
        for(int i=s.size()-1,w=1;i>=0;i--){
            res += (s[i]-'A'+1)*w;
            w *= 26;
        }
        return res;
    }
};
