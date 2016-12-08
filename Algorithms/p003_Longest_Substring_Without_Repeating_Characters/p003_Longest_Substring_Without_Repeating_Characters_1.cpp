class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> seen(256,-1); // seen[c]: index of seen c in s
        int max_len = 0;
        int cur_start = 0;
        int cur_len = 0;
        for(int i=0;i<s.size();++i){
            if(seen[s[i]]==-1){
                seen[s[i]] = i;
                ++cur_len;
                max_len = max(max_len,cur_len);
            }else{
                cur_len = i-seen[s[i]];
                for(int j=cur_start;j<seen[s[i]];++j){
                    seen[s[j]] = -1;
                }
                seen[s[i]] = i;
                cur_start = i-cur_len+1;
            }
        }
        return max_len;
    }
};
