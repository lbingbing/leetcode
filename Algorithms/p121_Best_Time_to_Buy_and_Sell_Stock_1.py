class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l<=1:
            return 0
        
        mins = [prices[0]]*(l-1)
        maxs = [prices[l-1]]*(l-1)
        for i in range(1,l-1):
            mins[i] = min(prices[i],mins[i-1])
        for i in range(l-3,-1,-1):
            maxs[i] = max(prices[i+1],maxs[i+1])
        res = 0
        for i in range(0,l-1):
            res = max(maxs[i]-mins[i],res)
        return res
