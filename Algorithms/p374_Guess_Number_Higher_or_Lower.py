# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n+1
        while True:
            mid = l+(r-l)//2
            comp = guess(mid)
            if comp<0:
                r = mid
            elif comp>0:
                l = mid+1
            else:
                return mid
        return 0 # dummy return
