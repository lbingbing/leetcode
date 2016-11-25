class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty()) return "";
        string s = strs[0];
        for(int i=1;i<strs.size();++i){
            int j = 0;
            while(j<strs[i].size()&&j<s.size()&&strs[i][j]==s[j]) ++j;
            s.resize(j);
            if(s.empty()) return "";
        }
        return s;
    }
};
