class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        state = []
        self.combinationSum3Helper(res,state,k,n,1)
        return res
        
    def combinationSum3Helper(self, res, state, k, n, start):
        if k>0:
            i = max(start,n-(20-k)*(k-1)//2)
            while (i*2+k-1)*k//2<=n:
                state.append(i)
                self.combinationSum3Helper(res,state,k-1,n-i,i+1)
                del state[-1]
                i += 1
        else:
            res.append(state[:])
