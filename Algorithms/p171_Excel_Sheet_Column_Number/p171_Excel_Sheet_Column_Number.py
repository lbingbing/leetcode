class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        w = 1
        res = 0
        ord_A = ord('A')
        for i in range(len(s)-1,-1,-1):
            res += (ord(s[i])-ord_A+1)*w
            w *= 26
        return res
