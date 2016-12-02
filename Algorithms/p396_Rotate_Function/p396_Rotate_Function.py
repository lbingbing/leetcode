class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        sum_A = 0
        F = 0
        for i in range(n):
            sum_A += A[i]
            F += i*A[i]
        res = F
        for i in range(1,n):
            # F(i)-F(j)=sum(A)-nA[n-i], 0<=i<=n-1, j=(i-1)%n
            F += sum_A-n*A[n-i]
            if F>res:
                res = F
        return res
