class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]*(rowIndex+1)
        for i in range(1,rowIndex+1):
            old_v = res[0]
            for j in range(1,i):
                res[j],old_v = old_v+res[j],res[j]
        return res
