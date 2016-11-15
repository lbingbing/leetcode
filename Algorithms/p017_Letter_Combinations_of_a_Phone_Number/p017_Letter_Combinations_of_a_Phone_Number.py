class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        for c in digits:
            if c not in map(lambda x:str(x),range(0,10)):
                return []
        res = []
        mapping = [' ',
                   '*',
                   'abc',
                   'def',
                   'ghi',
                   'jkl',
                   'mno',
                   'pqrs',
                   'tuv',
                   'wxyz']
        cur = []
        self.dfs(res,mapping,cur,digits,0)
        return res

    def dfs(self, res, mapping, cur, digits, pos):
        if pos<len(digits):
            d = int(digits[pos])
            for i in range(0,len(mapping[d])):
                cur.append(mapping[d][i])
                self.dfs(res,mapping,cur,digits,pos+1)
                cur.pop()
        else:
            res.append(''.join(cur))
