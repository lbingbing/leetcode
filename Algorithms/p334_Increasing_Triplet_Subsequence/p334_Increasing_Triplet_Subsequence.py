class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        v1 = float('inf')
        v2 = float('inf')
        for v in nums:
            if v<=v1:
                v1 = v
            elif v<=v2:
                v2 = v
            else:
                return True
        return False
