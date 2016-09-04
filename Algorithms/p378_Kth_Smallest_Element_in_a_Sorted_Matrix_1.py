class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m_len = len(matrix)
        for i in range(0,k-1):
            matrix[0][0] = None
            j1 = 0
            j2 = 0
            while j1<m_len and j2<m_len:
                v1 = matrix[j1+1][j2] if j1!=m_len-1 else None
                v2 = matrix[j1][j2+1] if j2!=m_len-1 else None
                if v1!=None and (v2==None or v1<=v2):
                    matrix[j1][j2],matrix[j1+1][j2] = v1,None
                    j1 += 1
                elif v2!=None and (v1==None or v2<=v1):
                    matrix[j1][j2],matrix[j1][j2+1] = v2,None
                    j2 += 1
                else:
                    break
        return matrix[0][0]
