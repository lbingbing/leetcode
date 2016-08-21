class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        res = [None] * nums_len
        res[0] = 1
        for i in range(1,nums_len):
            res[i] = res[i-1] * nums[i-1]
        r_product = nums[-1]
        for i in range(nums_len-2,-1,-1):
            res[i] *= r_product
            r_product *= nums[i]
        return res
