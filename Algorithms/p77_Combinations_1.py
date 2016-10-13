class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.combineHelper(n,k,1)
        
    def combineHelper(self, n, k, start):
        if start>n or k==0:
            return [[]]
        res = self.combineHelper(n,k-1,start+1)
        for e in res:
            e.insert(0,start)
        if n-start>=k:
            res1 = self.combineHelper(n,k,start+1)
            res += res1
        return res
