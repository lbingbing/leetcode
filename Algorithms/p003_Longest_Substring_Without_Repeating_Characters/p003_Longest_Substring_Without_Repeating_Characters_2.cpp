class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> index(256,-1); // index[c]: index of c in s so far
        int max_len = 0;
        for(int i=0,start=0;i<s.size();++i){
            start = max(start,index[s[i]]+1);
            max_len = max(max_len,i-start+1);
            index[s[i]] = i;
        }
        return max_len;
    }
};
