class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt1 = [0]*256
        cnt2 = [0]*256
        for c in s:
            cnt1[ord(c)] += 1
        for c in t:
            cnt2[ord(c)] += 1
        return cnt1==cnt2
