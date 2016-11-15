class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b&0xffffffff==0:
            if(not a&0x80000000):
                return a&0xffffffff
            else:
                return -((~a&0xffffffff)+1)
        else:
            return self.getSum(a^b,(a&b)<<1)
