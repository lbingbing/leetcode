class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        res = []
        cur = []
        self.partitionHelper(res,cur,s,0)
        return res

    def partitionHelper(self, res, cur, s, start):
        for i in range(start,len(s)):
            # check palindrome
            l = start
            r = i
            while l<r:
                if s[l]!=s[r]:
                    break
                l += 1
                r -= 1
            if l<r:
                continue
            # dfs search
            cur.append(s[start:i+1])
            if i<len(s)-1:
                self.partitionHelper(res,cur,s,i+1)
            else:
                res.append(cur[:])
            cur.pop()
