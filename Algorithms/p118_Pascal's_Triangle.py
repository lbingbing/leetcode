class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        res = [[] for i in range(0,numRows)]
        res[0].append(1)
        for i in range(1,numRows):
            res[i].append(1)
            for j in range(1,i):
                res[i].append(res[i-1][j-1]+res[i-1][j])
            res[i].append(1)
        return res
