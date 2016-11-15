class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        s_l = len(s)
        j = 0
        while True:
            i = j
            while j<s_l and not (ord(s[j])>=ord('0') and ord(s[j])<=ord('9')):
                j += 1
            l.append(s[i:j])
            if j==s_l:
                break
            i = j
            j += 1
            while ord(s[j])>=ord('0') and ord(s[j])<=ord('9'):
                j += 1
            num = int(s[i:j])
            # s[j]=='['
            open_brackets = 1
            j += 1
            i = j
            while True:
                if s[j]=='[':
                    open_brackets += 1
                elif s[j]==']':
                    open_brackets -= 1
                    if open_brackets==0:
                        break;
                j += 1
            l.append(self.decodeString(s[i:j])*num)
            j += 1
        return ''.join(l)
