class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        l = [(len(s),set(s)) for s in words]
        res = 0
        for i1 in range(0,len(words)-1):
            for i2 in range(i1+1,len(words)):
                v = l[i1][0]*l[i2][0]
                if v>res:
                    if len(l[i1][1])>len(l[i2][1]):
                        s_l = l[i1][1]
                        s_s = l[i2][1]
                    else:
                        s_l = l[i2][1]
                        s_s = l[i1][1]
                    has_common_letter = 0
                    for c in s_s:
                        if c in s_l:
                            has_common_letter = 1
                            break
                    if not has_common_letter:
                        res = v
        return res
