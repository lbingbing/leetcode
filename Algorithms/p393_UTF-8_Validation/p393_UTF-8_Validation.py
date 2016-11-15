class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        left_cnt = 0
        for v in data:
            if left_cnt==0:
                if (v&0x80)==0:
                    pass
                elif (v&0xe0)==0xc0:
                    left_cnt = 1
                elif (v&0xf0)==0xe0:
                    left_cnt = 2
                elif (v&0xf8)==0xf0:
                    left_cnt = 3
                else:
                    return False
            else:
                if (v&0xc0)!=0x80:
                    return False
                left_cnt -= 1
        return left_cnt==0
