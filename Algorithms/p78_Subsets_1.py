class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums:
            nums1 = nums[:-1]
            res = self.subsets(nums1)
            res1 = [e[:] for e in res]
            for e in res1:
                e.append(nums[-1])
            res += res1
            return res
        else:
            return [[]]
