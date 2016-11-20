class Solution {
public:
    string countAndSay(int n) {
        string s("1");
        while(--n>0){
            string s1;
            int pos = 0;
            while(pos<s.size()){
                int start = pos;
                while(pos<s.size()&&s[pos]==s[start]) ++pos;
                s1 += to_string(pos-start)+s[start];
            }
            s = move(s1);
        }
        return s;
    }
};
