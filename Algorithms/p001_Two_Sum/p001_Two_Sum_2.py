class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums1 = list(enumerate(nums))
        nums1.sort(key=lambda x:x[1])
        l = 0
        r = len(nums1)-1
        while l<r:
            sum1 = nums1[l][1]+nums1[r][1]
            if sum1<target:
                l += 1
            elif sum1>target:
                r -= 1
            else:
                return [min(nums1[l][0],nums1[r][0]),max(nums1[l][0],nums1[r][0])]
        return [] # dummy return
