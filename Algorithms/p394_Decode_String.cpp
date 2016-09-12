class Solution {
public:
    string decodeString(string s) {
        string res;
        int len = s.size();
        int j = 0;
        while(1){
            int i = j;
            while(j<len && !(s[j]>='0' && s[j]<='9')){
                ++j;
            }
            res.append(s,i,j-i);
            if(j==len){
                break;
            }
            i = j;
            ++j;
            while(s[j]>='0' && s[j]<='9'){
                ++j;
            }
            int num = stoi(s.substr(i,j-i));
            // s[j]=='['
            int open_brackets = 1;
            ++j;
            i = j;
            while(1){
                if(s[j]=='['){
                    ++open_brackets;
                }else if(s[j]==']'){
                    --open_brackets;
                    if(open_brackets==0){
                        break;
                    }
                }
                ++j;
            }
            string s1 = decodeString(s.substr(i,j-i));
            for(int k=0;k<num;++k){
                res += s1;
            }
            ++j;
        }
        return res;
    }
};
