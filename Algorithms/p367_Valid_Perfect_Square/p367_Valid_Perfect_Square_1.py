class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while True:
            i2 = i**2
            if i2==num:
                return True
            elif i2>num:
                break
            i += 1
        return False
