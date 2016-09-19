class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num<0 or num>10:
            return []
        
        values = [[[] for i in range(0,7)] for i in range(0,7)] # table[width][ones]={values}
        for e in values:
            e[0].append(0)
        for i in range(1,len(values)):
            values[i][i].append((1<<i)-1)
        for i in range(2,len(values)):
            for j in range(1,i):
                values[i][j] += values[i-1][j]
                values[i][j] += [v+(1<<(i-1)) for v in values[i-1][j-1]]
        
        res = []
        for i in range(max(0,num-6),min(4,num)+1):
            for h in values[4][i]:
                if h<12:
                    for m in values[6][num-i]:
                        if m<60:
                            res.append(str(h)+":"+str(m).zfill(2))
        return res
