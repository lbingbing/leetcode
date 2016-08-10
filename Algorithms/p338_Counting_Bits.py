class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        l = [0]*(num+1)
        m = 1
        m2 = 2
        for i in range(1,num+1):
            if i < m2:
                l[i] = l[i-m] + 1
            else:
                l[i] = 1
                m = m2
                m2 = m*2
        return l
