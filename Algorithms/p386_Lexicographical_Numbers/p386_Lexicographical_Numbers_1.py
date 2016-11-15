class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [None]*n
        i = 0
        m = 1
        while i<n:
            res[i] = m
            i += 1
            m *= 10
            while m>n:
                m //= 10
                m += 1
                while m%10==0:
                    m //= 10
        return res
