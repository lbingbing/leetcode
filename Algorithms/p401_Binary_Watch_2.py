class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num<0 or num>10:
            return []
        
        values1 = [[] for i in range(0,5)]
        for i in range(0,12):
            values1[self.countOnes(i)].append(str(i))
        values2 = [[] for i in range(0,7)]
        for i in range(0,60):
            values2[self.countOnes(i)].append(str(i).zfill(2))
        
        res = []
        for i in range(max(0,num-6),min(4,num)+1):
            for h in values1[i]:
                for m in values2[num-i]:
                    res.append(h+":"+m)
        return res
        
    def countOnes(self, v):
        num = 0
        for i in range(0,32):
            if v&0x1:
                num += 1
            v >>= 1
        return num
