class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            a = '0'
        if not b:
            b = '0'
        res = []
        i = len(a)-1
        j = len(b)-1
        c = 0
        while i>=0 or j>=0:
            op1 = int(a[i]) if i>=0 else 0
            op2 = int(b[j]) if j>=0 else 0
            out = op1+op2+c
            res.append('1' if out&0x1 else '0')
            c = 1 if out>=2 else 0
            if i>=0:
                i -= 1
            if j>=0:
                j -= 1
        if c>0:
            res.append('1')
        return ''.join(reversed(res))
