class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        if s_len:
            l = [0]*(s_len+1)
            for i in range(0,s_len):
                if s[i]=='I': l[i] = 1
                elif s[i]=='V': l[i] = 5
                elif s[i]=='X': l[i] = 10
                elif s[i]=='L': l[i] = 50
                elif s[i]=='C': l[i] = 100
                elif s[i]=='D': l[i] = 500
                elif s[i]=='M': l[i] = 1000
                else: l[i] = 0
            l[s_len] = 0
            res = 0
            inc_start = 0
            last_v = l[0]
            for i in range(1,s_len+1):
                if l[i]<=last_v:
                    if inc_start<i-1:
                        res -= sum(l[inc_start:i-1])
                    res += l[i-1]
                    inc_start = i
                last_v = l[i]
            return res
        else:
            return 0
