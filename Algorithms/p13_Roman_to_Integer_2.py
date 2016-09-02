class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        l = [0]*s_len
        for i in range(0,s_len):
            if s[i]=='I': l[i] = 1
            elif s[i]=='V': l[i] = 5
            elif s[i]=='X': l[i] = 10
            elif s[i]=='L': l[i] = 50
            elif s[i]=='C': l[i] = 100
            elif s[i]=='D': l[i] = 500
            elif s[i]=='M': l[i] = 1000
            else: l[i] = 0
        for i in range(1,s_len):
            if l[i]>l[i-1]:
                l[i-1] = -l[i-1]
        return sum(l)
