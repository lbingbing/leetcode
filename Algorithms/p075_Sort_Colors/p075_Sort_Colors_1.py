class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = [0]*3
        for v in nums:
            cnt[v] += 1
        i = 0
        for j in range(0,3):
            while cnt[j]>0:
                nums[i] = j
                i += 1
                cnt[j] -= 1
