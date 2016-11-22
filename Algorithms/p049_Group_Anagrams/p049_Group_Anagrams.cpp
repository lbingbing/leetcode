class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hash_table;
        for(auto &s : strs){
            string s1(s);
            sort(s1.begin(),s1.end());
            hash_table[s1].push_back(s);
        }
        vector<vector<string>> res;
        for(auto &e : hash_table){
            res.push_back(move(e.second));
        }
        return res;
    }
};
