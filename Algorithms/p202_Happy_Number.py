class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        table = [False]*811
        while True:
            m = 0
            while n:
                m += (n%10)**2
                n //= 10
            n = m
            if n==1:
                return True
            if table[n]:
                return False
            else:
                table[n] = True
        return False # dummy
