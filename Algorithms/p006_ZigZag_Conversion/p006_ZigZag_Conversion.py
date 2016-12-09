class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1:
            return s
        n = len(s)
        m = numRows*2-2
        l = [s[0:n:m]]
        for i in range(1,numRows-1):
            j = i
            d = m-i*2
            while j<n:
                l.append(s[j])
                j += d
                d = m-d
        l.append(s[numRows-1:n:m])
        return ''.join(l)
