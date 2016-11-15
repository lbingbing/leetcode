class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        l_mask = 1
        h_mask = 1
        x1 = x
        while x1>=10:
            x1 //= 10
            h_mask *= 10
        while l_mask<h_mask:
            if (x//l_mask)%10!=(x//h_mask)%10:
                return False
            l_mask *= 10
            h_mask //= 10
        return True
