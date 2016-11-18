class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t<0:
            return False
        d = dict()
        w = t+1
        for i in range(len(nums)):
            if i>k:
                key = nums[i-k-1]//w
                del d[key]
            key = nums[i]//w
            if key in d:
                return True
            if key-1 in d and nums[i]-d[key-1]<=t:
                return True
            if key+1 in d and d[key+1]-nums[i]<=t:
                return True
            d[key] = nums[i]
        return False
