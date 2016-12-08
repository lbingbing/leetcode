class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {chr(i):-1 for i in range(256)} # index[c]: index of c in s so far
        max_len = 0
        start = 0
        for i in range(len(s)):
            start = max(start,index[s[i]]+1)
            max_len = max(max_len,i-start+1)
            index[s[i]] = i
        return max_len
