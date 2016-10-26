class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        j = len(height)-1
        while i<j:
            l = height[i]
            r = height[j]
            res = max(res,(j-i)*min(l,r))
            if l<=r:
                while i<j and height[i]<=l:
                    i += 1
            if l>=r:
                while i<j and height[j]<=r:
                    j -= 1
        return res
