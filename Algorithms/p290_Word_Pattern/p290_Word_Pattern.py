class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        mapping = [None]*256
        str_seen = set()
        s_list = str.split()
        if len(pattern)!=len(s_list):
            return False
        for c,s in zip(pattern,s_list):
            c = ord(c)
            if mapping[c]!=s:
                if mapping[c]==None:
                    if s not in str_seen:
                        str_seen.add(s)
                    else:
                        return False
                    mapping[c] = s;
                else:
                    return False
        return True
