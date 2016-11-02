class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        cnt = [0]*(n+1)
        for v in citations:
            if v>n:
                cnt[n] += 1
            else:
                cnt[v] += 1
        for i in range(n,-1,-1):
            if cnt[i]>=i:
                return i
            cnt[i-1] += cnt[i]
        return 0 # dummy return
