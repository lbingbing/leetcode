class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        upper_bound = 2**n
        res = [0]*upper_bound
        for i in range(0,upper_bound):
            for j in range(0,n):
                res[i] |= ((i>>1)&(0x1<<j))^(i&(0x1<<j))
        return res
