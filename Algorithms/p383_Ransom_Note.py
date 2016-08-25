class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        len1 = len(ransomNote)
        len2 = len(magazine)
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        i = 0
        j = 0
        while i<len1 and j<len2:
            if ransomNote[i]==magazine[j]:
                i += 1
                j += 1
            elif ransomNote[i]>magazine[j]:
                j += 1
            else:
                break
        return i==len1
