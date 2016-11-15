class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {chr(i):None for i in range(256)}
        mapped = {chr(i):False for i in range(256)}
        for c1,c2 in zip(s,t):
            if mapping[c1]==None:
                mapping[c1] = c2
                if not mapped[c2]:
                    mapped[c2] = True
                else:
                    return False
            elif mapping[c1]!=c2:
                return False
        return True
