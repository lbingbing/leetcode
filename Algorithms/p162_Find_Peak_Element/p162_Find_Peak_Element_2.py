class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)
        while True:
            mid = (l+r)//2
            if (mid==0 or nums[mid]>nums[mid-1]) and (mid==len(nums)-1 or nums[mid]>nums[mid+1]):
                return mid
            elif (mid==0 or nums[mid]>nums[mid-1]) and (mid<len(nums)-1 and nums[mid]<nums[mid+1]):
                l = mid+1
            else:
                r = mid
        return -1 # dummy return
