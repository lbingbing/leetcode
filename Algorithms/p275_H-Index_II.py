class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l =0
        r = n
        while l<r:
            mid = (l+r)//2
            if citations[mid]<n-mid:
                l = mid+1
            elif citations[mid]>n-mid:
                r = mid
            else:
                return n-mid
        return n-l
