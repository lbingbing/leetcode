class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        
        res = 0;
        min_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i]>min_price:
                res = max(prices[i]-min_price,res)
            else:
                min_price = prices[i]
        return res
