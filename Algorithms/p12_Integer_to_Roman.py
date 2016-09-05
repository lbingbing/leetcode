class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        
        d = (num/1000)%10
        if d>=1 and d<=3:
            res.append('M'*d)
        
        d = (num/100)%10
        if d>=1 and d<=3:
            res.append('C'*d)
        elif d==4:
            res.append('CD')
        elif d>=5 and d<9:
            res.append('D'+'C'*(d-5))
        elif d==9:
            res.append('CM')
        
        d = (num/10)%10
        if d>=1 and d<=3:
            res.append('X'*d)
        elif d==4:
            res.append('XL')
        elif d>=5 and d<9:
            res.append('L'+'X'*(d-5))
        elif d==9:
            res.append('XC')
        
        d = num%10
        if d>=1 and d<=3:
            res.append('I'*d)
        elif d==4:
            res.append('IV')
        elif d>=5 and d<9:
            res.append('V'+'I'*(d-5))
        elif d==9:
            res.append('IX')
        
        return ''.join(res)
