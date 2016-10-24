class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = list(reversed(digits))
        carry = True
        for i in range(0,len(res)):
            res[i] += 1
            if res[i]==10:
                res[i] = 0
            else:
                carry = False
                break
        if carry:
            res.append(1)
        res.reverse()
        return res
