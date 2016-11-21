class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda e: (e[0],-e[1]))
        # min_h[i]: min h of i-length sequence's last envelope so far
        min_h = [0]*(len(envelopes)+1)
        max_len = 0
        for e in envelopes:
            j = bisect.bisect_left(min_h,e[1],0,max_len+1)
            min_h[j] = e[1]
            max_len = max(max_len,j)
        return max_len
