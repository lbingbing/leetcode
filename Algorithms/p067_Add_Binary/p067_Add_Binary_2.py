class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2) if a else 0
        b = int(b,2) if b else 0
        return '{:b}'.format(a+b)
