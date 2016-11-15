class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l==0:
            return 0
        
        forward_max = [0]*l
        lowest = prices[0]
        for i in range(1,l):
            forward_max[i] = max(forward_max[i-1],prices[i]-lowest)
            lowest = min(lowest,prices[i])
        
        backward_max = [0]*l
        highest = prices[l-1]
        for i in range(l-2,-1,-1):
            backward_max[i] = max(backward_max[i+1],highest-prices[i])
            highest = max(highest,prices[i])
        
        res = 0
        for i in range(0,l):
            res = max(res,forward_max[i]+backward_max[i])
        return res
