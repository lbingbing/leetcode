class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        m = len(p)
        if n<m:
            return []
        res = []
        cnt_p = {chr(ord('a')+i):0 for i in range(26)}
        for c in p:
            cnt_p[c] += 1
        cnt = {chr(ord('a')+i):0 for i in range(26)}
        for i in range(0,m):
            cnt[s[i]] += 1
        if cnt==cnt_p:
            res.append(0)
        for i in range(1,n-m+1):
            cnt[s[i-1]] -= 1
            cnt[s[i+m-1]] += 1
            if cnt==cnt_p:
                res.append(i)
        return res
