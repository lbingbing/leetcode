class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.findPeakElementHelper(nums,0,len(nums))

    def findPeakElementHelper(self, nums, l, r):
        mid = (l+r)//2
        if (mid==0 or nums[mid]>nums[mid-1]) and (mid==len(nums)-1 or nums[mid]>nums[mid+1]):
            return mid
        elif (mid==0 or nums[mid]>nums[mid-1]) and (mid<len(nums)-1 and nums[mid]<nums[mid+1]):
            return self.findPeakElementHelper(nums,mid+1,r)
        else:
            return self.findPeakElementHelper(nums,l,mid)
