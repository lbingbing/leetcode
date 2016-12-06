class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        unordered_map<string,int> cnt;
        for(int i=10;i<=s.size();++i){
            string s1(s,i-10,10);
            if(++cnt[s1]==2) res.push_back(s1);
        }
        return res;
    }
};
