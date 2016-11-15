class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0;
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            x = nums[mid]
            if nums[l]>x:
                r = mid
            elif x>nums[r]:
                l = mid+1
            else:
                break
        return nums[l]
