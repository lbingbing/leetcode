class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = set()
        seen = set()
        for i in range(10,len(s)+1):
            s1 = s[i-10:i]
            key = 0
            for c in s1:
                key <<= 2
                if c=='A':
                    key |= 0x0
                elif c=='C':
                    key |= 0x1
                elif c=='G':
                    key |= 0x2
                elif c=='T':
                    key |= 0x3
            if key in seen:
                res.add(s1)
            else:
                seen.add(key)
        return list(res)
