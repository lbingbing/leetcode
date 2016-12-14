class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        while i<len(str) and str[i]==' ':
            i += 1
        if i<len(str):
            res = 0
            positive = True
            if str[i]=='+':
                i += 1
            elif str[i]=='-':
                positive = False
                i += 1
            while i<len(str):
                if '0'<=str[i]<='9':
                    res = res*10+int(str[i])
                    if res>2147483647:
                        return 2147483647 if positive else -2147483648
                    i += 1
                else:
                    break
            return res if positive else -res
        return 0
