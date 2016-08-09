class Solution {
public:
    string reverseString(string s) {
        string s1(s);
        int len = s1.size();
        int n = len/2;
        for(int i=0;i<n;i++){
            char c = s1[i];
            s1[i] = s1[len-1-i];
            s1[len-1-i] = c;
        }
        return s1;
    }
};
