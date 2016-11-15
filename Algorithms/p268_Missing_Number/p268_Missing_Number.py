class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = [False]*(len(nums)+1)
        for v in nums:
            cnt[v] = True
        for i in range(0,len(cnt)):
            if not cnt[i]:
                return i
        return -1
