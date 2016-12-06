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
            if s1 in seen:
                res.add(s1)
            else:
                seen.add(s1)
        return list(res)
