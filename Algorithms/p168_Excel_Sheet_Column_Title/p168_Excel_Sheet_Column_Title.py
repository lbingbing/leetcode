class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        l = []
        ord_A = ord('A')
        while True:
            n -= 1
            l.append(chr(ord_A+n%26))
            n //= 26
            if not n:
                break
        l.reverse()
        return ''.join(l)
