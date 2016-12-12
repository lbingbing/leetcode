class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        x1 = abs(x)
        while x1:
            res = res*10+x1%10
            x1 //= 10
        return (res if x>=0 else -res) if res>=-2147483648 and res<=2147483647 else 0
