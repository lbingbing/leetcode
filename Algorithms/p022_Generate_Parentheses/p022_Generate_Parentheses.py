class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generateParenthesisStep(res,'',n,n)
        return res
        
    def generateParenthesisStep(self, res, s, l, r):
        if l==0 and r==0:
            res.append(s)
        else:
            if l:
                self.generateParenthesisStep(res,s+'(',l-1,r)
            if r>l:
                self.generateParenthesisStep(res,s+')',l,r-1)
