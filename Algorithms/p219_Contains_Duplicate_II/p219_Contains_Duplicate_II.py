class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pos = min(len(nums),k+1)
        s = set(nums[:pos])
        if len(s)<pos:
            return True
        for i in range(pos,len(nums)):
            # remove before add for cases where nums[i-k-1]==nums[i]
            s.remove(nums[i-k-1])
            s.add(nums[i])
            if len(s)<k+1:
                return True
        return False
