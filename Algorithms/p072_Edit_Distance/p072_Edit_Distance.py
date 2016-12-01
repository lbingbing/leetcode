class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(word1)
        n2 = len(word2)
        # num[i][j]: min distance from word1[0...i-1] to word2[0...j-1]
        num = [[None for j in range(n2+1)] for i in range(n1+1)]
        for i in range(n1+1):
            num[i][0] = i
        for j in range(1,n2+1):
            num[0][j] = j
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                num[i][j] = min(num[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1),num[i-1][j]+1,num[i][j-1]+1)
        return num[n1][n2]
