class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        p_table = [[False for j in range(n)] for i in range(m)]
        a_table = [[False for j in range(n)] for i in range(m)]
        q_p = collections.deque()
        q_a = collections.deque()
        for i in range(m):
            if not p_table[i][0]:
                p_table[i][0] = True
                q_p.append((i,0))
            if not a_table[i][n-1]:
                a_table[i][n-1] = True
                q_a.append((i,n-1))
        for j in range(n):
            if not p_table[0][j]:
                p_table[0][j] = True
                q_p.append((0,j))
            if not a_table[m-1][j]:
                a_table[m-1][j] = True
                q_a.append((m-1,j))
        self.flood(matrix,p_table,q_p,m,n)
        self.flood(matrix,a_table,q_a,m,n)
        res = []
        for i in range(m):
            for j in range(n):
                if p_table[i][j] and a_table[i][j]:
                    res.append([i,j])
        return res

    def flood(self, matrix, table, q, m, n):
        while q:
            i = q[0][0]
            j = q[0][1]
            q.popleft()
            if i>0 and not table[i-1][j] and matrix[i][j]<=matrix[i-1][j]:
                table[i-1][j] = True
                q.append((i-1,j))
            if i<m-1 and not table[i+1][j] and matrix[i][j]<=matrix[i+1][j]:
                table[i+1][j] = True
                q.append((i+1,j))
            if j>0 and not table[i][j-1] and matrix[i][j]<=matrix[i][j-1]:
                table[i][j-1] = True
                q.append((i,j-1))
            if j<n-1 and not table[i][j+1] and matrix[i][j]<=matrix[i][j+1]:
                table[i][j+1] = True
                q.append((i,j+1))
