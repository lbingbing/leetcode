class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 1
        r = num+1
        while l<r:
            mid = (l+r)//2
            q = num//mid
            if mid<q:
                l = mid+1
            elif mid>q:
                r = mid
            else:
                return mid**2==num
        return False
