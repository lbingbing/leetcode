class Solution {
public:
    bool wordPattern(string pattern, string str) {
        vector<string> mapping(256);
        unordered_set<string> str_seen;
        int pos1 = 0;
        int pos2 = 0;
        int pos2_start;
        while(1){
            while(pos2<str.size()&&str[pos2]==' ') ++pos2;
            if(pos2>=str.size()) break;
            if(pos1>=pattern.size()) break;
            pos2_start = pos2;
            while(pos2<str.size()&&str[pos2]!=' ') ++pos2;
            char c = pattern[pos1++];
            string s = str.substr(pos2_start,pos2-pos2_start);
            if(mapping[c]!=s){
                if(mapping[c].size()==0){
                    if(!str_seen.insert(s).second) return 0;
                    mapping[c] = s;
                }else{
                    return 0;
                }
            }
        }
        return pos1==pattern.size()&&pos2==str.size();
    }
};
