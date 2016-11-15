class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if(digits.empty()) return {};
        for(char c : digits){
            if(c<'2'||c>'9') return {};
        }
        vector<string> res;
        vector<vector<char>> mapping = {{'a','b','c'},
                                        {'d','e','f'},
                                        {'g','h','i'},
                                        {'j','k','l'},
                                        {'m','n','o'},
                                        {'p','q','r','s'},
                                        {'t','u','v'},
                                        {'w','x','y','z'}};
        string cur;
        dfs(res,mapping,cur,digits,0);
        return res;
    }
    void dfs(vector<string>& res, vector<vector<char>>& mapping, string& cur, string& digits, int pos) {
        if(pos<digits.size()){
            int d = digits[pos]-'0'-2;
            for(int i=0;i<mapping[d].size();++i){
                cur.push_back(mapping[d][i]);
                dfs(res,mapping,cur,digits,pos+1);
                cur.pop_back();
            }
        }else{
            res.push_back(cur);
        }
    }
};
