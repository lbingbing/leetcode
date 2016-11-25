class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        s = strs[0]
        for i in range(1,len(strs)):
            j = 0
            while j<len(strs[i]) and j<len(s) and strs[i][j]==s[j]:
                j += 1
            s = s[:j]
            if not s:
                return s
        return s
