class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        n -= 1
        while n>0:
            s1 = []
            pos = 0
            while pos<len(s):
                start = pos
                while pos<len(s) and s[pos]==s[start]:
                    pos += 1
                s1.append(str(pos-start))
                s1.append(s[start])
            s = ''.join(s1)
            n -= 1
        return s
