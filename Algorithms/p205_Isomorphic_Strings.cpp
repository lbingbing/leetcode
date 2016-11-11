class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int n = s.size();
        vector<int> mapping(256,-1);
        vector<bool> mapped(256,0);
        for(int i=0;i<n;++i){
            auto c1 = s[i];
            auto c2 = t[i];
            if(mapping[c1]==-1){
                mapping[c1] = c2;
                if(!mapped[c2]) mapped[c2] = 1;
                else return 0;
            }else if(mapping[c1]!=c2){
                return 0;
            }
        }
        return 1;
    }
};
