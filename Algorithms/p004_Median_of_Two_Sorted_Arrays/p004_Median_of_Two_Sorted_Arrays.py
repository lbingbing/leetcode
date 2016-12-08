class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)<len(nums2):
            nums1,nums2 = nums2,nums1
        n1 = len(nums1)
        n2 = len(nums2)
        k = (n1+n2+1)//2
        double_median = ((n1+n2)%2==0)
        l1 = 0
        r1 = n1
        l2 = 0
        r2 = n2
        while l1<r1:
            mid = (l1+r1)//2
            pos = bisect.bisect_left(nums2,nums1[mid],l2,r2)
            k1 = mid+pos+1
            if k1<k:
                l1 = mid+1
                l2 = pos
            elif k1>k:
                r1 = mid
                r2 = pos
            else:
                median = nums1[mid]
                if double_median:
                    if mid+1>=n1:
                        median2 = nums2[pos]
                    elif pos>=n2:
                        median2 = nums1[mid+1]
                    else:
                        median2 = min(nums1[mid+1],nums2[pos])
                    return (median+median2)/2.0
                return median
        median = nums2[k-l1-1]
        if double_median:
            if l1>=n1:
                median2 = nums2[k-l1]
            elif k-l1>=n2:
                median2 = nums1[l1]
            else:
                median2 = min(nums1[l1],nums2[k-l1])
            return (median+median2)/2.0
        return median
