class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1_1 = nums1[:]
        j1 = 0
        j2 = 0
        for i in range(0,m+n):
            if j1<m and (j2==n or nums1_1[j1]<nums2[j2]):
                nums1[i] = nums1_1[j1]
                j1 += 1
            else:
                nums1[i] = nums2[j2]
                j2 += 1
