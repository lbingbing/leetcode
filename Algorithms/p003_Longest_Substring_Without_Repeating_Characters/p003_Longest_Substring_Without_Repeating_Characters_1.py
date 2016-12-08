class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {chr(i):-1 for i in range(0,256)} # seen[c]: index of seen c in s
        max_len = 0
        cur_start = 0
        cur_len = 0
        for i in range(len(s)):
            if seen[s[i]]==-1:
                seen[s[i]] = i
                cur_len += 1
                max_len = max(max_len,cur_len)
            else:
                cur_len = i-seen[s[i]]
                for j in range(cur_start,seen[s[i]]):
                    seen[s[j]] = -1
                seen[s[i]] = i
                cur_start = i-cur_len+1
        return max_len
