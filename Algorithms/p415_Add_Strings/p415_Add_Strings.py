class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l = max(len(num1),len(num2))
        res = []
        j1 = len(num1)-1
        j2 = len(num2)-1
        carry = 0
        ord_0 = ord('0')
        for i in range(0,l):
            din1 = ord(num1[j1])-ord_0 if j1>=0 else 0
            din2 = ord(num2[j2])-ord_0 if j2>=0 else 0
            dout = din1+din2+carry
            carry = 1 if dout>=10 else 0
            dout = dout-10 if dout>=10 else dout
            res += chr(ord_0+dout)
            if j1>=0:
                j1 -= 1
            if j2>=0:
                j2 -= 1
        if carry==1:
            res += '1'
        res.reverse()
        return ''.join(res)
