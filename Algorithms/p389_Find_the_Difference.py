class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cnt = [0]*265
        for c in s:
            cnt[ord(c)] += 1
        for c in t:
            if cnt[ord(c)]==0:
                return c
            cnt[ord(c)] -= 1
        return chr(0)
