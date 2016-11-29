class Solution {
public:
    vector<vector<string>> partition(string s) {
        if(s.empty()) return {{}};
        vector<vector<string>> res;
        vector<string> cur;
        partitionHelper(res,cur,s,0);
        return res;
    }
    void partitionHelper(vector<vector<string>>& res, vector<string>& cur, string& s, int start) {
        for(int i=start;i<s.size();++i){
            // check palindrome
            int l = start;
            int r = i;
            for(;l<r;++l,--r){
                if(s[l]!=s[r]) break;
            }
            if(l<r) continue;
            // dfs search
            cur.push_back(s.substr(start,i-start+1));
            if(i<s.size()-1) partitionHelper(res,cur,s,i+1);
            else             res.push_back(cur);
            cur.pop_back();
        }
    }
};
