class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l_max = [0]*n
        r_max = [0]*n
        for i in range(1,n):
            l_max[i] = max(l_max[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            r_max[i] = max(r_max[i+1],height[i+1])
        res = 0
        for i in range(1,n-1):
            res += max(min(l_max[i],r_max[i])-height[i],0)
        return res
