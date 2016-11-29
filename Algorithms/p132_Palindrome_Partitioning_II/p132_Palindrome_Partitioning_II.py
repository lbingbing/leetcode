class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        cut_num = [None]*(n+1) #// cut_num[i]: min cut num of s[0,i-1]
        isPalindrome = [[None for j in range(n)] for i in range(n)] # isPalindrome[i][j]: s[i,j] is palindrome
        cut_num[0] = -1
        for j in range(n):
            cut_num[j+1] = j
            for i in range(j+1):
                isPalindrome[i][j] = (s[i]==s[j] and (i+1>=j-1 or isPalindrome[i+1][j-1]))
                if isPalindrome[i][j]:
                    cut_num[j+1] = min(cut_num[j+1],cut_num[i]+1)
        return cut_num[n]
