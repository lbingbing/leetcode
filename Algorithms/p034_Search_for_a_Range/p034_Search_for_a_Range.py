class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = self.binarySearch(nums,target,1)
        if start>=len(nums) or nums[start]>target:
            return [-1,-1]
        end = self.binarySearch(nums,target,0)
        return [start,end-1]

    def binarySearch(self, nums, target, lower):
        l = 0
        r = len(nums)
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid
            else:
                if lower:
                    r = mid
                else:
                    l = mid+1
        return l
