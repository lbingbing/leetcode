class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        start = 0
        length = 1
        isPalindrome = [[True]*n for i in range(n)]
        for i in range(1,n):
            for j in range(i+1):
                isPalindrome[j][i] = (s[i]==s[j]) and (j+1>i-1 or isPalindrome[j+1][i-1])
                if isPalindrome[j][i] and i-j+1>=length:
                    start = j
                    length = i-j+1
        return s[start:start+length]
