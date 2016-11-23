class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = len(s)-1
        while pos>=0 and s[pos]==' ':
            pos -= 1
        end = pos
        while pos>=0 and s[pos]!=' ':
            pos -= 1
        return end-pos
