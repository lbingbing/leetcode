class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = [0]*256
        for c in s:
            cnt[ord(c)] += 1
        res = 0
        has_odd = 0
        for num in cnt:
            res += num//2*2
            has_odd |= num&0x1
        return res+has_odd
