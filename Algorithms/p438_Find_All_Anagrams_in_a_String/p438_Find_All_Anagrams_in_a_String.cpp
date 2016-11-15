class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int n = s.size();
        int m = p.size();
        if(n<m) return {};
        vector<int> res;
        vector<int> cnt_p(256,0);
        for(int i=0;i<m;++i){
            ++cnt_p[p[i]];
        }
        vector<int> cnt(256,0);
        for(int i=0;i<m;++i){
            ++cnt[s[i]];
        }
        if(equal(cnt.begin(),cnt.end(),cnt_p.begin())){
            res.push_back(0);
        }
        for(int i=1;i<=n-m;++i){
            --cnt[s[i-1]];
            ++cnt[s[i+m-1]];
            if(equal(cnt.begin(),cnt.end(),cnt_p.begin())){
                res.push_back(i);
            }
        }
        return res;
    }
};
