class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        i = 0
        j = len(s)-1
        while True:
            while i<j and l[i] not in 'aeiouAEIOU':
                i += 1
            while i<j and l[j] not in 'aeiouAEIOU':
                j -= 1
            if i<j:
                l[i],l[j] = l[j],l[i]
            else:
                break
            i += 1
            j -= 1
        return ''.join(l)
