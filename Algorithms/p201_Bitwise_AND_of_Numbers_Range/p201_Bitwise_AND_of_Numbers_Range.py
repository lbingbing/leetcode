class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(31):
            group_size = 0x1<<(i+1)
            half_group_size = 0x1<<i
            if m//group_size==n//group_size and m%group_size>=half_group_size:
                res |= 0x1<<i
        return res
