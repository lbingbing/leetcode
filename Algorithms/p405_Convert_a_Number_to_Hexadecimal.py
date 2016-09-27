class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num!=0:
            n = num if num>=0 else 0x100000000+num
            res = ''
            while n!=0:
                d = n&0xf
                if d>=0 and d<10:
                    res = chr(ord('0')+d)+res
                else:
                    res = chr(ord('a')+d-10)+res
                n >>= 4
            return res
        else:
            return '0'
