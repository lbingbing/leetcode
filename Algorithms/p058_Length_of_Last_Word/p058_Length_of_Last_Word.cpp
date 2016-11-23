class Solution {
public:
    int lengthOfLastWord(string s) {
        int pos = s.size()-1;
        while(pos>=0&&s[pos]==' ') --pos;
        int end = pos;
        while(pos>=0&&s[pos]!=' ') --pos;
        return end-pos;
    }
};
