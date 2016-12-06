class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        unordered_map<int,int> cnt;
        for(int i=10;i<=s.size();++i){
            int key = 0;
            for(int j=i-10;j<i;++j){
                key <<= 2;
                switch(s[j]){
                    case 'A': key |= 0x0; break;
                    case 'C': key |= 0x1; break;
                    case 'G': key |= 0x2; break;
                    case 'T': key |= 0x3; break;
                }
            }
            ++cnt[key];
            if(cnt[key]==2) res.push_back(s.substr(i-10,10));
        }
        return res;
    }
};
