class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        n = len(nums)
        l = 0
        r = n
        left_most = nums[l]
        while l<r:
            mid = l+(r-l)//2
            if nums[mid]<left_most:
                r = mid
            else:
                l = mid+1
        p = l # start of 2nd part, or n when no rotation
        if target>=nums[0] and target<=nums[p-1]:
            l = 0
            r = p
        elif p<n and target>=nums[p] and target<=nums[n-1]:
            l = p
            r = n
        else:
            return -1
        while l<r:
            mid = l+(r-l)//2
            if target<nums[mid]:
                r = mid
            elif target>nums[mid]:
                l = mid+1
            else:
                return mid
        return -1
