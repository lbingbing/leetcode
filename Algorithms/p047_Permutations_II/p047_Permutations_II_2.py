class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        return self.permuteUniqueHelper(nums)

    def permuteUniqueHelper(self, nums):
        if not nums:
            return [[]]
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            nums1 = nums[0:i]+nums[i+1:]
            res1 = self.permuteUniqueHelper(nums1)
            for e in res1:
                e.insert(0,nums[i])
            res += res1
        return res
