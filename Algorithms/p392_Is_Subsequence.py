class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len1 = len(s)
        len2 = len(t)
        i = 0
        j = 0
        while i<len1 and j<len2:
            if s[i]==t[j]:
                i += 1
            j += 1
        return i==len1
