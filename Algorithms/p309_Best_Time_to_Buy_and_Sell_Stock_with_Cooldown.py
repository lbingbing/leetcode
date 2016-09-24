class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l<=1:
            return 0
        s0 = [None]*l # not holding
        s1 = [None]*l # holding
        s2 = [None]*l # just sold
        s0[0] = 0
        s1[0] = -prices[0]
        for i in range(1,l):
            s0[i] = max(s0[i-1],s2[i-1]) if i>1 else s0[0]
            s1[i] = max(s0[i-1]-prices[i],s1[i-1])
            s2[i] = s1[i-1]+prices[i]
        return max(s0[l-1],s2[l-1])
