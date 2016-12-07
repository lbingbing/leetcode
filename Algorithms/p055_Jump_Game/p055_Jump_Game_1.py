class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_reachable = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=min_reachable:
                min_reachable = i
        return min_reachable==0
