class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        heap = [(v,i) for i,v in enumerate(matrix[0])]
        ptr = [0]*m
        heapq.heapify(heap)
        for i in range(0,k-1):
            col = heap[0][1]
            ptr[col] += 1
            p = ptr[col]
            if p<m:
                heapq.heapreplace(heap,(matrix[p][col],heap[0][1]))
            else:
                heapq.heappop(heap)
        return heap[0][0]
