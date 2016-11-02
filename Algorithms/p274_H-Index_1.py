class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        cnt = 0
        for v in citations:
            cnt += 1
            if v<cnt:
                cnt -= 1
            if v<=cnt:
                break
        return cnt
